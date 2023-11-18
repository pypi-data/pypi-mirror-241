# pylint: disable=R0902,R0903

"""Base for Connectors."""

from __future__ import annotations

import itertools
import json
import logging
import re
import time
from operator import itemgetter
from queue import Queue
from threading import Thread
from typing import Callable
from urllib.parse import urlencode

import requests
from requests import Session, Response
from requests.exceptions import ReadTimeout, ConnectionError as RequestsConnectionError
from vhelpers import vdict, vlist, vparam

from vpnetbox import helpers as h
from vpnetbox.exceptions import NbApiError
from vpnetbox.types_ import DAny, DStr, LDAny, SStr, LStr, DLInt, DList
from vpnetbox.types_ import TLists, OUParam, SeqStr, OSeqStr, LParam


class BaseC:
    """Base for Connectors."""

    path = ""
    _slices = [
        "id",
        "name",
        "slug",
        "display",
        "prefix",
        "address",
        "cid",
        "vid",
        "asn",
    ]
    _init_params = [
        "host",
        "token",
        "scheme",
        "port",

        "verify",
        "limit",
        "url_max_len",
        "threads",
        "interval",
        "max_items",

        "timeout",
        "max_retries",
        "sleep",
    ]
    _reserved_ipam_keys = [
        "overlapped",
        "warnings",
        "nbnets",
        "nbnets__subnets",
    ]

    def __init__(self, **kwargs):
        """Init BaseC.

        :param host: Netbox host name.
        :param token: Netbox token.
        :param scheme: Access method: https or http. Default "https".
        :param port: TCP port. Default 443. NOTE: Not implemented.

        :param verify: Transport Layer Security. True - A TLS certificate required,
            False - Requests will accept any TLS certificate.
        :param limit: Split the query to multiple requests if the response exceeds the limit.
            Default 1000.
        :param url_max_len: Split the query to multiple requests if the URL length exceeds
            this value. Default 3900.
        :param threads: Threads count. Default 1, loop mode.
        :param interval: Wait this time between requests (seconds).
            Default 0. Useful for request speed shaping.
        :param max_items: Stop the request if received items reach this value.
            Default unlimited. Useful if you need many objects but not all.

        :param timeout: Request timeout (seconds). Default 60.
        :param max_retries: Retry the request multiple times if it receives a 500 error
            or timed-out. Default 1.
        :param sleep: Interval before the next retry after receiving a 500 error (seconds).
            Default 10.
        """
        self.host: str = _init_host(**kwargs)
        self.token: str = str(kwargs.get("token") or "")
        self.scheme: str = _init_scheme(**kwargs)
        self.port: int = int(kwargs.get("port") or 0)

        self.verify: bool = _init_verify(**kwargs)
        self.limit: int = int(kwargs.get("limit") or 1000)
        self.max_items: int = int(kwargs.get("max_items") or 0)
        self.timeout: float = float(kwargs.get("timeout") or 60)
        self.max_retries: int = int(kwargs.get("max_retries") or 1)
        self.sleep: float = float(kwargs.get("sleep") or 10)
        self.calls_interval: float = float(kwargs.get("sleep") or 0)
        self.threads: int = _init_threads(**kwargs)
        self.interval: float = float(kwargs.get("interval") or 0.0)
        self.url_max_len = int(kwargs.get("url_max_len") or 3900)

        self.default: DAny = {}  # default params
        self._session: Session = requests.session()
        self._parallels: LStr = ["q", "status", "tag"]  # need parallel requests
        self._param_id_map: DAny = self._init_param_id_map()
        self._results: LDAny = []  # cache for received objects from Netbox

    def _init_param_id_map(self) -> DAny:
        """Init a dictionary that maps model name to their corresponding new path.

        This mapping is used to get objects from Netbox by name instead of id.
        :return: Dictionary with mapping data.
        """
        data = {
            # circuits
            "circuit": {"path": "circuits/circuits/", "key": "cid"},
            "provider": {"path": "circuits/providers/", "key": "name"},
            "provider_account": {"path": "circuits/provider-accounts/", "key": "name"},
            # dcim
            "platform": {"path": "dcim/platforms/", "key": "name"},
            "region": {"path": "dcim/regions/", "key": "name"},
            "site": {"path": "dcim/sites/", "key": "name"},
            "site_group": {"path": "dcim/site-groups/", "key": "name"},
            # extras
            "content_type": {"path": "extras/content-types/", "key": "display"},
            "for_object_type": {"path": "extras/content-types/", "key": "display"},
            # ipam
            "export_target": {"path": "ipam/route-targets/", "key": "name"},
            "exporting_vrf": {"path": "ipam/vrfs/", "key": "name"},
            "import_target": {"path": "ipam/route-targets/", "key": "name"},
            "importing_vrf": {"path": "ipam/vrfs/", "key": "name"},
            "present_in_vrf": {"path": "ipam/vrfs/", "key": "name"},
            "rir": {"path": "ipam/rirs/", "key": "name"},
            "vrf": {"path": "ipam/vrfs/", "key": "name"},
            # tenancy
            "tenant": {"path": "tenancy/tenants/", "key": "name"},
            "tenant_group": {"path": "tenancy/tenant-groups/", "key": "name"},
            # virtualization
            "bridge": {"path": "virtualization/interfaces/", "key": "name"},
        }

        group_map = {
            "dcim/sites/": {"group": {"path": "dcim/site-groups/", "key": "name"}},
            "ipam/vlans/": {"group": {"path": "ipam/vlan-groups/", "key": "name"}},
            "tenancy/tenants/": {"group": {"path": "tenancy/tenant-groups/", "key": "name"}},
            "virtualization/clusters/": {
                "group": {"path": "virtualization/cluster-groups/", "key": "name"}},
        }
        if data_ := group_map.get(self.path):
            data.update(data_)

        parent_map = {
            "dcim/locations/": {"parent": {"path": "dcim/locations/", "key": "name"}},
            "dcim/regions/": {"parent": {"path": "dcim/regions/", "key": "name"}},
            "dcim/site-groups/": {"parent": {"path": "dcim/site-groups/", "key": "name"}},
            "tenancy/tenant-groups/": {"parent": {"path": "tenancy/tenant-groups/", "key": "name"}},
            "virtualization/interfaces/": {
                "parent": {"path": "virtualization/interfaces/", "key": "name"}},
        }
        if data_ := parent_map.get(self.path):
            data.update(data_)

        # role
        if self.path == "virtualization/virtual-machines/":
            data.update({
                "role": {"path": "dcim/device-roles/", "key": "name"},
            })
        else:
            data.update({
                "role": {"path": "ipam/roles/", "key": "name"},
            })

        # type
        if self.path == "circuits/circuits/":
            data.update({
                "type": {"path": "circuits/circuit-types/", "key": "name"},
            })

        return data

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        return f"<{name}: {self.host}>"

    # ============================= property =============================

    @property
    def url(self) -> str:
        """Base URL with the application and model path."""
        return f"{self.url_base}{self.path}"

    @property
    def url_base(self) -> str:
        """Base URL without the application and model path."""
        return f"{self.scheme}://{self.host}/api/"

    # ============================= methods ==============================

    def create(self, **params: dict) -> Response:
        """Create object in Netbox.

        :param params: Parameters of new object.
        :return: Session response.
            *<Response [201]>* Object successfully created,
            *<Response [400]>* Object already exist.
        """
        response: Response = self._session.post(
            url=self.url,
            data=json.dumps(params),
            headers=self._headers(),
            verify=self.verify,
            timeout=self.timeout,
        )
        return response

    def create_d(self, **params: dict) -> DAny:
        """Create object in Netbox.

        :param params: Parameters of new object.
        :return: Dictionary of crated object.
        """
        response: Response = self.create(**params)
        if not response.status_code == 201:
            return {}
        html: str = response.content.decode("utf-8")
        data: DAny = dict(json.loads(html))
        return data

    # noinspection PyShadowingBuiltins
    def delete(self, id: int) -> Response:  # pylint: disable=redefined-builtin
        """Delete object in Netbox.

        :param id: Object ID.
        :return: Session response. *<Response [204]>* Object successfully deleted,
            *<Response [404]>* Object not found.
        """
        response: Response = self._session.delete(
            url=f"{self.url}{id}",
            headers=self._headers(),
            verify=self.verify,
            timeout=self.timeout,
        )
        return response

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get list of dictionaries from Netbox.

        :param q: Substring in: main value, slug, description.
        """
        params: LDAny = self._validate_params(**kwargs)

        items: LDAny = self._query_params_ld(params)

        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items

    def query(self, path: str, params: OUParam = None) -> LDAny:
        """Retrieve data from Netbox.

        :param path: Section of the URL that points to the model.
        :param params: Parameters to request from Netbox.
        :return: A list of the Netbox objects.
        :example:
            query(path="ipam/ip-addresses/", params=[("status", "active")]) ->
            [{"id": 1, "address": "", ...}, ...]
        """
        if params is None:
            params = []
        params_d = vparam.to_dict(params)
        return self._query_loop(path, params_d)

    def query_count(self, params: LParam) -> int:
        """Get count of Netbox objects."""
        response: Response = self._session.get(
            url=f"{self.url}?{urlencode(params)}",
            headers=self._headers(),
            verify=self.verify,
            timeout=self.timeout,
        )
        if not response.ok:
            return 0
        html: str = response.content.decode("utf-8")
        count = int(json.loads(html)["count"])
        return count

    def update(self, **params: dict) -> Response:
        """Update object in Netbox.

        :param params: Parameters to update object in Netbox, "id" is required.
        :return: Session response. *<Response [200]>* Object successfully updated,
            *<Response [400]>* Invalid data.
        """
        id_ = vdict.pop("id", params)
        if not id_:
            raise ValueError("id expected in the data.")

        response: Response = self._session.patch(
            url=f"{self.url}{id_}/",
            data=json.dumps(params),
            headers=self._headers(),
            verify=self.verify,
            timeout=self.timeout,
        )
        return response

    def update_d(self, **params: dict) -> DAny:
        """Update object in Netbox.

        :param params: Parameters to update object in Netbox, "id" is required.
        :return: Dictionary of updated object.
        """
        response: Response = self.update(**params)
        if not response.status_code == 200:
            return {}
        html: str = response.content.decode("utf-8")
        data: DAny = dict(json.loads(html))
        return data

    # ============================== query ===============================

    def _query_params_ld(self, params: LDAny) -> LDAny:
        """Retrieve data from Netbox.

        :param params: Parameters to request from Netbox.
        :return: A list of the Netbox objects.
        """
        self._results = []
        params_ld: LDAny = h.slice_params_ld(self.url, self.url_max_len, self._slices, params)

        # threads
        if self.threads > 1:
            counts_w_params: LDAny = self._query_pages_count(params_ld)
            params_ld = self._slice_params_counters(counts_w_params)
            self._query_threads(method=self._query_data_thread, params=params_ld)
        # loop
        else:
            for params_d in params_ld:
                results_: LDAny = self._query_loop(self.path, params_d)
                self._results.extend(results_)

        # save
        results: LDAny = sorted(self._results, key=itemgetter("id"))
        results = vlist.no_dupl(results)
        self._results = []
        return results

    def _query_count(self, path: str, params_d: DAny) -> None:
        """Retrieve counters of interested objects from Netbox.

        :param path: Section of the URL that points to the model.
        :param params_d: Parameters to request from Netbox.
        :return: None. Update self object.
        """
        params_d_ = params_d.copy()
        params_d_["brief"] = 1
        params_d_["limit"] = 1
        params_l: LParam = vparam.from_dict(params_d_)
        url = f"{self.url_base}{path}?{urlencode(params_l)}"
        response: Response = self.retry_requests(url)

        count = 0
        if response.ok:
            html: str = response.content.decode("utf-8")
            data: DAny = json.loads(html)
            count = int(data["count"])

        result = {"count": count, "params_d": params_d}
        self._results.append(result)

    def _query_loop(self, path: str, params_d: DAny) -> LDAny:
        """Retrieve data from Netbox in loop mode.

        If the number of items in the result exceeds the limit, iterate through the offset
        in a loop mode.
        :param path: Section of the URL that points to the model.
        :param params_d: Parameters to request from Netbox.
        :return: Netbox objects. Update self _results.
        """
        if not params_d.get("limit"):
            params_d["limit"] = self.limit
        params_l: LParam = vparam.from_dict(params_d)
        offset = 0

        results: LDAny = []
        while True:
            params_i = [*params_l, ("offset", offset)]
            url = f"{self.url_base}{path}?{urlencode(params_i)}"
            response: Response = self.retry_requests(url)
            if response.ok:
                html: str = response.content.decode("utf-8")
                data: DAny = json.loads(html)
                results_: LDAny = list(data["results"])
                results.extend(results_)
            else:
                results_ = []

            # stop requests if limit reached
            if self.limit != len(results_):
                break
            if self.max_items and self.max_items <= len(results):
                break

            # next iteration
            if self.interval:
                time.sleep(self.interval)
            offset += self.limit

        return results

    def _query_data_thread(self, path: str, params_d: DAny) -> None:
        """Retrieve data from Netbox.

        If the number of items in the result exceeds the limit, iterate through the offset
        in a loop mode.
        :param path: Section of the URL that points to the model.
        :param params_d: Parameters to request from Netbox.
        :return: Netbox objects. Update self _results.
        """
        params_l: LParam = vparam.from_dict(params_d)
        url = f"{self.url_base}{path}?{urlencode(params_l)}"
        response: Response = self.retry_requests(url)
        if response.ok:
            html: str = response.content.decode("utf-8")
            data: DAny = json.loads(html)
            results_: LDAny = list(data["results"])
            self._results.extend(results_)

    def _query_pages_count(self, params: LDAny) -> LDAny:
        """Retrieve counters of interested objects from Netbox in threaded mode.

        :param params: Parameters to request from Netbox.
        :return: List of dict with counters and parameters of interested objects.
        """
        self._results = []
        self._query_threads(method=self._query_count, params=params)
        results: LDAny = self._results
        self._results = []
        return results

    def _query_threads(self, method: Callable, params: LDAny) -> None:
        """Retrieve data from Netbox in threaded mode.

        :param method: Method that need call with parameters.
        :param params: Parameters to request from Netbox.
        :return: None. Save results to self._results.
        """
        queue: Queue = Queue()
        for params_d in params:
            queue.put((method, params_d))

        for idx in range(self.threads):
            if self.interval:
                time.sleep(self.interval)
            thread = Thread(name=f"Thread-{idx}", target=self._run_queue, args=(queue,))
            thread.start()
        queue.join()

    def _run_queue(self, queue: Queue) -> None:
        """Process tasks from the queue.

        This method dequeues and executes tasks until the queue is empty.
        Each task is expected to be a callable method with its corresponding params_d parameters.
        :param queue: A queue containing (method, params_d) pairs to be executed.
        :return: None. Update self _results list.
        """
        while not queue.empty():
            method, params_d = queue.get()
            method(self.path, params_d)
            queue.task_done()

    def retry_requests(self, url: str) -> Response:
        """Retry multiple requests if the session times out.

        Multiple requests are useful if Netbox is overloaded and cannot process the request
        right away, but can do so after a sleep interval.

        :param url: The URL that needs to be requested.
        :return: The response.
        :raise: ConnectionError if the limit of retries is reached.
        """
        counter = 0
        while counter < self.max_retries:
            counter += 1
            try:
                response: Response = self._session.get(
                    url=url,
                    headers=self._headers(),
                    verify=self.verify,
                    timeout=self.timeout,
                )
            except ReadTimeout:
                attempts = f"{counter} of {self.max_retries}"
                msg = f"Session timeout={self.timeout!r}sec reached, {attempts=}."
                logging.warning(msg)
                if counter < self.max_retries:
                    msg = f"Next attempt after sleep={self.sleep}sec."
                    logging.warning(msg)
                    time.sleep(self.sleep)
                continue
            except RequestsConnectionError as ex:
                raise ConnectionError(f"Netbox connection error: {ex}") from ex

            if response.ok:
                return response
            msg = self._msg_status_code(response)
            msg.lstrip(".")
            if self._is_status_code_500(response):
                raise ConnectionError(f"Netbox server error: {msg}.")
            if self._is_credentials_error(response):
                raise ConnectionError(f"Netbox credentials error: {msg}.")
            if self._is_not_available_error(response):
                logging.warning(msg)
                return response
            raise ConnectionError(f"ConnectionError: {msg}.")

        msg = f"max_retries={self.max_retries!r} reached."
        logging.warning(msg)
        response = Response()
        response.status_code = 504  # Gateway Timeout
        response._content = str.encode(msg)  # pylint: disable=protected-access
        return response

    # ============================== helper ==============================

    def _get_d(self) -> DAny:
        """Get dictionary from Netbox.

        :return: Dictionary.
        :raise: ConnectionError if status_code is not 200.
        """
        response: Response = self.retry_requests(url=self.url)
        if response.ok:
            html: str = response.content.decode("utf-8")
            return dict(json.loads(html))

        # error
        msg = self._msg_status_code(response)
        raise ConnectionError(f"Netbox server error: {msg}")

    def _get_l(self) -> LDAny:
        """Get list from Netbox.

        :return: List of dictionary.
        :raise: ConnectionError if status_code is not 200.
        """
        response: Response = self.retry_requests(url=self.url)
        if response.ok:
            html: str = response.content.decode("utf-8")
            return list(json.loads(html))

        # error
        msg = self._msg_status_code(response)
        raise ConnectionError(f"Netbox server error: {msg}")

    def _validate_params(self, **kwargs) -> LDAny:
        """Validate and update params.

        Remove duplicates, convert single items to list, replace {name} to {name}_id,
        split the parallel parameters into separate items.
        :param kwargs: Filter parameters to update.
        :return: Updated parameters.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        kwargs = _lists_wo_dupl(kwargs)
        params_ld: LDAny = _make_combinations(self._parallels, kwargs)
        params = self._join_params(*params_ld)
        return params

    def _headers(self) -> DStr:
        """Session headers with token."""
        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json"
        }
        return headers

    def _join_params(self, *params) -> LDAny:
        """Join received and default filtering parameters.

        :param params: Received filtering parameters.
        :return: Joined filtering parameters.
        """
        if not params:
            return [self.default.copy()]

        params_: LDAny = []
        default_keys = sorted(list(self.default), reverse=True)
        for params_d in params:
            for key in default_keys:
                if params_d.get(key) is None:
                    params_d = {**{key: self.default[key]}, **params_d}
            params_.append(params_d)
        return params_

    @staticmethod
    def _check_keys(items: LDAny, denied: OSeqStr = None) -> None:
        """Check if denied keys are absent in the data.

        The Netbox REST API returns the object as a dictionary.
        Some of my dirty scripts inject extra key/value pairs into this object.
        I need to make sure that these keys are not used in Netbox.

        :return: True if all denied keys are absent in the data, otherwise if a denied key is
            found in the object.
        """
        if denied is None:
            denied = []

        denied_keys: SStr = set()
        for data in items:
            for key in denied:
                if key in data:
                    denied_keys.add(key)
                    msg = f"Denied {key=} in Netbox {data=}"
                    logging.error(msg)
        if denied_keys:
            raise NbApiError(f"Netbox data contains {denied_keys=}")

    def _slice_params_counters(self, results: LDAny) -> LDAny:
        """Generate sliced parameters based on counts in results.

        To request data in threading mode need have all params with offsets.
        :param results: List of dicts with params_d and related counts of objects.
        :return: Sliced parameters.
        """
        params: LDAny = []
        for result in results:
            count = result["count"]
            params_d = result["params_d"]
            if not result["count"]:
                continue
            if count <= self.limit:
                params.append(params_d)
                continue
            params_: LDAny = h.generate_offsets(count, self.limit, params_d)
            params.extend(params_)
        return params

    # ============================== is ==============================

    @staticmethod
    def _is_status_code_400(response: Response) -> bool:
        """Return True if status_code 4xx."""
        if 400 <= response.status_code < 500:
            return True
        return False

    @staticmethod
    def _is_status_code_500(response: Response) -> bool:
        """Return True if status_code 5xx."""
        if 500 <= response.status_code < 600:
            return True
        return False

    @staticmethod
    def _is_credentials_error(response: Response) -> bool:
        """Return True if invalid credentials."""
        if response.status_code == 403:
            if re.search("Invalid token", response.text, re.I):
                return True
        return False

    @staticmethod
    def _is_not_available_error(response: Response) -> bool:
        """Return True if the object (tag) absent in Netbox."""
        if response.status_code == 400:
            return True
        return False

    # =========================== messages ===========================

    @staticmethod
    def _msg_status_code(response: Response) -> str:
        """Return message ready for logging ConnectionError."""
        if not hasattr(response, "status_code"):
            return ""
        status_code, text, url = response.status_code, response.text, response.url

        pattern = "Page Not Found."
        if re.search(f"<title>{pattern}.+", text):
            text = pattern

        return f"{status_code=} {text=} {url=}"

    # ======================== params helpers ========================

    def _change_param_name_to_id(self, params_d: DAny) -> DAny:
        """Change parameter with name to parameter with id.

        Request all related objects from Netbox, find the name, and replace it with the ID.
        :param params_d: Parameters that need to update.
        :return: Updated parameters.
        """
        need_delete: LStr = []
        need_add: DLInt = {}
        for name, value in params_d.items():
            values = vlist.to_list(value)
            if name in self._param_id_map:
                path = self._param_id_map[name]["path"]
                key = self._param_id_map[name]["key"]

                response: LDAny = self.query(path=path)

                if ids := [d["id"] for d in response if d[key] in values]:
                    need_delete.append(name)
                    name_id = f"{name}_id"
                    need_add.setdefault(name_id, []).extend(ids)

        params_d_ = {k: v for k, v in params_d.items() if k not in need_delete}
        params_d_.update(need_add)
        return params_d_


# ============================= helpers ==========================

def _init_host(**kwargs) -> str:
    """Init Netbox host name."""
    host = str(kwargs.get("host") or "")
    if not host:
        raise ValueError("Host is required.")
    return host


def _init_scheme(**kwargs) -> str:
    """Init scheme "https" or "http"."""
    scheme = str(kwargs.get("scheme") or "https")
    expected = ["https", "http"]
    if scheme not in expected:
        raise ValueError(f"{scheme=}, {expected=}")
    return scheme


def _init_threads(**kwargs) -> int:
    """Init threads count, default 1."""
    threads = int(kwargs.get("threads") or 1)
    threads = max(threads, 1)
    return int(threads)


def _init_verify(**kwargs) -> bool:
    """Init verify. False - Requests will accept any TLS certificate."""
    verify = kwargs.get("verify")
    if verify is None:
        return True
    return bool(verify)


def _lists_wo_dupl(kwargs: DAny) -> DAny:
    """Convert single values to list and remove duplicate values from params.

    :param kwargs: A dictionary containing the parameters with single or multiple values.
    :return: A dictionary with list of values where duplicates removed.
    """
    params_d: DAny = {}
    for key, value in kwargs.items():
        if isinstance(value, TLists):
            params_d[key] = vlist.no_dupl(list(value))
        else:
            params_d[key] = [value]
    return params_d


def _make_combinations(parallels: SeqStr, params_d: DAny) -> LDAny:
    """Split the parallel parameters from the kwargs dictionary to valid combinations.

    :param parallels: A list of parallel parameters.
    :param params_d: A dictionary of keyword arguments.
    :return: A list of dictionaries containing the valid combinations.
    """
    keys_w_parallel: LStr = sorted(set(params_d).intersection(set(parallels)))
    wo_parallel = {k: v for k, v in params_d.items() if k not in keys_w_parallel}

    key_wo_parallel = ""
    w_parallel_d: DList = {}
    for key, values in params_d.items():
        if key in keys_w_parallel:
            for value in values:
                w_parallel_d.setdefault(key, []).append({key: [value]})
        else:
            key_wo_parallel = key

    parallel_l = list(w_parallel_d.values())
    if key_wo_parallel:
        parallel_l.append([wo_parallel])

    combinations = list(itertools.product(*parallel_l))

    params_ld = []
    for combination in combinations:
        params_d_ = {}
        for param_d_ in combination:
            params_d_.update(param_d_)
        if params_d_:
            params_ld.append(params_d_)
    return params_ld
