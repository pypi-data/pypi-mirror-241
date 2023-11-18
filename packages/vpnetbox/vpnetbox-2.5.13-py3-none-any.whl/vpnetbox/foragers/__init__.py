# pylint: disable=R0902,R0913

"""NbForager."""

from __future__ import annotations

import copy
import logging
from datetime import datetime
from pathlib import Path

from vhelpers import vstr

from vpnetbox import nb_tree
from vpnetbox.branch import NbBranch
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.circuits import CircuitsFA
from vpnetbox.foragers.core import CoreFA
from vpnetbox.foragers.dcim import DcimFA
from vpnetbox.foragers.extras import ExtrasFA
from vpnetbox.foragers.ipam import IpamFA
from vpnetbox.foragers.tenancy import TenancyFA
from vpnetbox.foragers.users import UsersFA
from vpnetbox.foragers.virtualization import VirtualizationFA
from vpnetbox.foragers.wireless import WirelessFA
from vpnetbox.messages import Messages
from vpnetbox.nb_cache import NbCache
from vpnetbox.nb_tree import NbTree, insert_tree
from vpnetbox.types_ import LStr, DAny, DiDAny, OUStr


class NbForager:
    """Forages data from Netbox to the NbForager.root object.

    Join objects within itself as a multidimensional dictionary in NbForager.tree object.
    You can access any associated object using dictionary keys.
    Write/read objects to/from the cache file.
    """

    def __init__(  # pylint: disable=R0914
            self,
            cache: str = "",

            host: str = "",
            token: str = "",
            scheme: str = "https",
            port: int = 0,

            verify: bool = True,
            limit: int = 1000,
            url_max_len: int = 3900,
            threads: int = 1,
            interval: float = 0.0,
            max_items: int = 0,

            # Error processing parameters
            timeout: int = 60,
            max_retries: int = 1,
            sleep: int = 10,
            **kwargs,
    ):
        """Init NbForager.

        :param cache: Path to cache. If the value ends with .pickle, it is the path to a file;
        otherwise, it is the path to a directory. The default value is NbCache.{hostname}.pickle.

        :param host: Netbox host name.
        :param token: Netbox token.
        :param scheme: Access method: https or http. Default "https".
        :param port: TCP port. Default 443. Not implemented.

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
        kwargs = {
            "host": host,
            "token": token,
            "scheme": scheme,
            "port": port,
            "verify": verify,
            "limit": limit,
            "url_max_len": url_max_len,
            "threads": threads,
            "interval": interval,
            "max_items": max_items,
            "timeout": timeout,
            "max_retries": max_retries,
            "sleep": sleep,
            **kwargs,
        }
        self.api = NbApi(**kwargs)
        self.cache: str = make_cache_path(cache, **kwargs)
        self.msgs = Messages(name=self.api.host)

        # data
        self.root: NbTree = NbTree()  # original data
        self.tree: NbTree = NbTree()  # data with joined objects within itself
        self.status: DAny = {}  # updated Netbox status data

        # foragers
        self.circuits = CircuitsFA(self.root, self.api)
        self.core = CoreFA(self.root, self.api)
        self.dcim = DcimFA(self.root, self.api)
        self.extras = ExtrasFA(self.root, self.api)
        self.ipam = IpamFA(self.root, self.api)
        self.tenancy = TenancyFA(self.root, self.api)
        self.users = UsersFA(self.root, self.api)
        self.virtualization = VirtualizationFA(self.root, self.api)
        self.wireless = WirelessFA(self.root, self.api)

    def __repr__(self) -> str:
        """__repr__."""
        attrs = list(NbTree().model_dump())
        params_d = {s: getattr(self, s).count() for s in attrs}
        params = vstr.repr_info(**params_d)
        name = self.__class__.__name__
        return f"<{name}: {params}>"

    def __copy__(self) -> NbForager:
        """Copy NbForager root and tree objects.

        :return: Copy of NbForager object.
        """
        connector = self.api.circuits.circuits
        params_d = {s: getattr(connector, s) for s in getattr(connector, "_init_params")}
        nbf = NbForager(**params_d)
        insert_tree(src=self.root, dst=nbf.root)
        return nbf

    @property
    def host(self) -> str:
        """Netbox host name."""
        return self.api.host

    @property
    def url(self) -> str:
        """Netbox URL."""
        return self.api.url

    # =========================== method =============================

    def count(self) -> int:
        """Count of the Netbox objects in the self root model.

        :return: Count of the Netbox objects.
        """
        counts = []
        for app in self.root.apps():
            count = getattr(self, app).count()
            counts.append(count)
        return sum(counts)

    def clear(self) -> None:
        """Clear objects by resetting the root and tree attributes."""
        for app in self.root.apps():
            for model in getattr(self.root, app).models():
                data: dict = getattr(getattr(self.root, app), model)
                data.clear()
        self.tree = NbTree()

    def copy(self) -> NbForager:
        """Copy NbForager root and tree objects.

        :return: Copy of NbForager object.
        """
        return copy.copy(self)

    def read_cache(self) -> None:
        """Read cached data from a pickle file and restore recursions in Net objects.

        :return: None. Update self object.
        """
        cache = NbCache(cache=self.cache)
        tree, status = cache.read_cache()
        insert_tree(src=tree, dst=self.root)
        self.status = status

    def write_cache(self) -> None:
        """Write cache to a pickle file..

        :return: None. Update a pickle file.
        """
        status: DAny = self.status.copy()
        status["meta"] = {
            "host": self.api.host,
            "url": self.api.url,
            "write_time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        }

        cache = NbCache(tree=self.root, status=status, cache=self.cache)
        cache.write_cache()

    def grow_tree(self) -> NbTree:
        """Join Netbox objects in tree within itself.

        The Netbox objects are represented as a multidimensional dictionary.
        :return: NbTree object with the joined data.
        """
        self.tree = nb_tree.grow_tree(self.root)
        return self.tree

    def get_status(self) -> None:
        """Retrieve Netbox status data from Netbox.

        :return: None. Update self status.
        """
        status = self.api.status.get()
        if not isinstance(status, dict):
            status = {}
        self.status = status

    def version(self) -> str:
        """Get Netbox status version.

        :return: Netbox version if version >=3.* else "".
        """
        return str(self.status.get("netbox-version") or "0.0.0")

    # =========================== data methods ===========================

    def devices_primary_ip4(self) -> LStr:
        """Return the primary IPv4 addresses of Netbox devices with these settings.

        :return: primary_ip4 addresses of devices.
        """
        ip4s: LStr = []
        for device in self.root.dcim.devices.values():  # pylint: disable=E1101
            if ip4 := NbBranch(device).primary_ip4():
                ip4s.append(ip4)
        return ip4s

    def set_ipam_ip_addresses_mask_32(self) -> None:
        """Change mask to /32 for all Netbox ip-addresses.

        :return: None. Update self object.
        """
        for data in self.root.ipam.ip_addresses.values():  # pylint: disable=E1101
            if data["address"].find("/") >= 0:
                ip_ = data["address"].split("/")[0]
                data["address"] = ip_ + "/32"

    # ============================= helpers =============================

    def print_warnings(self) -> None:
        """Print WARNINGS if found some errors/warnings in data processing."""
        for app in self.root.apps():
            for model in getattr(self.root, app).models():
                nb_objects: DiDAny = getattr(getattr(self.root, app), model)
                for nb_object in nb_objects.values():
                    if warnings := nb_object.get("warnings") or []:
                        for warning in warnings:
                            logging.warning(warning)


# noinspection PyIncorrectDocstring
def make_cache_path(cache: str = "", **kwargs) -> str:
    """Make path to pickle file.

    :param cache: Path to pickle file.
    :param name: Parent object name.
    :param host: Netbox host name.
    :return: Path to cache pickle file.
    """
    if cache.endswith(".pickle"):
        return cache
    name = str(kwargs.get("name") or "")
    host = str(kwargs.get("host") or "")
    if not (name or host):
        name = NbCache().__class__.__name__
    file_items = [name, host, "pickle"]
    file_items = [s for s in file_items if s]
    name = ".".join(file_items)
    path = Path(cache, name)
    return str(path)
