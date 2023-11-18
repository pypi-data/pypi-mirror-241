# pylint: disable=R0801,R0902,R0913,R0915

"""NbApi, Python wrapper of Netbox REST API."""

from __future__ import annotations

from typing import Union

from vpnetbox.branch import NbBranch
from vpnetbox.connectors.circuits import CircuitsCA
from vpnetbox.connectors.core import CoreCA
from vpnetbox.connectors.dcim import DcimCA
from vpnetbox.connectors.extras import ExtrasCA
from vpnetbox.connectors.ipam import IpamCA
from vpnetbox.connectors.plugins_ca import PluginsCA
from vpnetbox.connectors.status import StatusC
from vpnetbox.connectors.tenancy import TenancyCA
from vpnetbox.connectors.users import UsersCA
from vpnetbox.connectors.virtualization import VirtualizationCA
from vpnetbox.connectors.wireless import WirelessCA
from vpnetbox.types_ import DAny

ConnectorA = Union[CircuitsCA, DcimCA, ExtrasCA, IpamCA, TenancyCA, VirtualizationCA]


class NbApi:
    """NbApi, Python wrapper of Netbox REST API.

    - In 'get' method you can use multiple filter parameters identical to those in the web interface
        filter form. Different parameters work like 'AND' operator, while multiple values in the
        same parameter work like an 'OR' operator.
    - Multithreading is used to request a bulk of data in fast mode.
    - Replaces an error-400 response with an empty result. For example, when querying addresses by
        tag, if there are no address objects with this tag in Netbox, the default Netbox API
        response is error-400. This package logs a warning and returns an ok-200 response with an
        empty list.
    - Retries the request multiple times if the Netbox API responds with a timed-out. This is useful
        for scheduled scripts in cron jobs, when the connection to Netbox server is not stable.
    - Slices the query to multiple requests if the URL length exceeds 4000 characters
        (due to a long list of GET parameters).

    All models (ipam.ip_addresses, dcim.devices, etc.) have 'get', 'create', 'update' and 'delete'
    methods. The 'create', 'update' and 'delete' methods are identical for all models,
    but the parameters for the 'get' method are different for each model.
    Only 'ipam.ip_addresses' is described in the README, but other models are implemented
    in a similar manner. To find available filter parameters for other models, you can use the
    Netbox Web UI filter page, `./examples`_ or simply try your luck with `REST API`_ or
    `/api/schema/swagger-ui`_.
    """

    def __init__(
            self,
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
        """Init NbApi.

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
        # circuits
        self.circuits = CircuitsCA(**kwargs)
        self.circuit_terminations = self.circuits.circuit_terminations
        self.circuit_types = self.circuits.circuit_types
        self.circuits_ = self.circuits.circuits  # overlap with self.circuits
        self.provider_accounts = self.circuits.provider_accounts
        self.provider_networks = self.circuits.provider_networks
        self.providers = self.circuits.providers
        # core
        self.core = CoreCA(**kwargs)
        self.data_files = self.core.data_files
        self.data_sources = self.core.data_sources
        self.jobs = self.core.jobs
        # dcim
        self.dcim = DcimCA(**kwargs)
        self.cable_terminations = self.dcim.cable_terminations
        self.cables = self.dcim.cables
        # connected_device, is not model
        self.console_port_templates = self.dcim.console_port_templates
        self.console_ports = self.dcim.console_ports
        self.console_server_port_templates = self.dcim.console_server_port_templates
        self.console_server_ports = self.dcim.console_server_ports
        self.device_bay_templates = self.dcim.device_bay_templates
        self.device_bays = self.dcim.device_bays
        self.device_roles = self.dcim.device_roles
        self.device_types = self.dcim.device_types
        self.devices = self.dcim.devices
        self.front_port_templates = self.dcim.front_port_templates
        self.front_ports = self.dcim.front_ports
        self.interface_templates = self.dcim.interface_templates
        self.interfaces = self.dcim.interfaces  # overlap with virtualization.interfaces
        self.inventory_item_roles = self.dcim.inventory_item_roles
        self.inventory_item_templates = self.dcim.inventory_item_templates
        self.inventory_items = self.dcim.inventory_items
        self.locations = self.dcim.locations
        self.manufacturers = self.dcim.manufacturers
        self.module_bay_templates = self.dcim.module_bay_templates
        self.module_bays = self.dcim.module_bays
        self.module_types = self.dcim.module_types
        self.modules = self.dcim.modules
        self.platforms = self.dcim.platforms
        self.power_feeds = self.dcim.power_feeds
        self.power_outlet_templates = self.dcim.power_outlet_templates
        self.power_outlets = self.dcim.power_outlets
        self.power_panels = self.dcim.power_panels
        self.power_port_templates = self.dcim.power_port_templates
        self.power_ports = self.dcim.power_ports
        self.rack_reservations = self.dcim.rack_reservations
        self.rack_roles = self.dcim.rack_roles
        self.racks = self.dcim.racks
        self.rear_port_templates = self.dcim.rear_port_templates
        self.rear_ports = self.dcim.rear_ports
        self.regions = self.dcim.regions
        self.site_groups = self.dcim.site_groups
        self.sites = self.dcim.sites
        self.virtual_chassis = self.dcim.virtual_chassis
        self.virtual_device_contexts = self.dcim.virtual_device_contexts
        # extras
        self.extras = ExtrasCA(**kwargs)
        self.bookmarks = self.extras.bookmarks
        self.config_contexts = self.extras.config_contexts
        self.config_templates = self.extras.config_templates
        self.content_types = self.extras.content_types
        self.custom_field_choice_sets = self.extras.custom_field_choice_sets
        self.custom_fields = self.extras.custom_fields
        self.custom_links = self.extras.custom_links
        self.export_templates = self.extras.export_templates
        self.image_attachments = self.extras.image_attachments
        self.journal_entries = self.extras.journal_entries
        self.object_changes = self.extras.object_changes
        self.reports = self.extras.reports
        self.saved_filters = self.extras.saved_filters
        self.scripts = self.extras.scripts
        self.tags = self.extras.tags
        self.webhooks = self.extras.webhooks
        # ipam
        self.ipam = IpamCA(**kwargs)
        self.aggregates = self.ipam.aggregates
        self.asn_ranges = self.ipam.asn_ranges
        self.asns = self.ipam.asns
        self.fhrp_group_assignments = self.ipam.fhrp_group_assignments
        self.fhrp_groups = self.ipam.fhrp_groups
        self.ip_addresses = self.ipam.ip_addresses
        self.ip_ranges = self.ipam.ip_ranges
        self.l2vpn_terminations = self.ipam.l2vpn_terminations
        self.l2vpns = self.ipam.l2vpns
        self.prefixes = self.ipam.prefixes
        self.rirs = self.ipam.rirs
        self.roles = self.ipam.roles
        self.route_targets = self.ipam.route_targets
        self.service_templates = self.ipam.service_templates
        self.services = self.ipam.services
        self.vlan_groups = self.ipam.vlan_groups
        self.vlans = self.ipam.vlans
        self.vrfs = self.ipam.vrfs
        # plugins
        self.plugins = PluginsCA(**kwargs)
        self.installed_plugins = self.plugins.installed_plugins
        # status
        self.status = StatusC(**kwargs)
        # tenancy
        self.tenancy = TenancyCA(**kwargs)
        self.contact_assignments = self.tenancy.contact_assignments
        self.contact_groups = self.tenancy.contact_groups
        self.contact_roles = self.tenancy.contact_roles
        self.contacts = self.tenancy.contacts
        self.tenant_groups = self.tenancy.tenant_groups
        self.tenants = self.tenancy.tenants
        # users
        self.users = UsersCA(**kwargs)
        self.config = self.users.config
        self.groups = self.users.groups
        self.permissions = self.users.permissions
        self.tokens = self.users.tokens
        self.users_ = self.users.users  # overlap with self.users
        # virtualization
        self.virtualization = VirtualizationCA(**kwargs)
        self.cluster_groups = self.virtualization.cluster_groups
        self.cluster_types = self.virtualization.cluster_types
        self.clusters = self.virtualization.clusters
        self.interfaces_ = self.virtualization.interfaces  # overlap with dcim.interfaces
        self.virtual_machines = self.virtualization.virtual_machines
        # wireless
        self.wireless = WirelessCA(**kwargs)
        self.wireless_lan_groups = self.wireless.wireless_lan_groups
        self.wireless_lans = self.wireless.wireless_lans
        self.wireless_links = self.wireless.wireless_links

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        return f"<{name}: {self.host}>"

    @property
    def host(self) -> str:
        """Netbox host name."""
        return self.circuits.circuit_terminations.host

    @property
    def url(self) -> str:
        """Netbox URL."""
        return self.circuits.circuit_terminations.url_base

    # =========================== method =============================

    def default_active(self) -> None:
        """Set default filter parameters for all objects.

        This is useful when you only need to work with active IPv4 objects.
        """
        # ipam
        self.ipam.aggregates.default = {"family": 4}
        self.ipam.ip_addresses.default = {"family": 4, "status": "active"}
        self.ip_ranges.default = {"family": 4, "status": ["active"]}
        self.ipam.prefixes.default = {"family": 4, "status": ["active", "container"]}
        self.ipam.vlans.default = {"status": "active"}
        # dcim
        self.dcim.devices.default = {"has_primary_ip": True, "status": "active"}
        self.dcim.sites.default = {"status": "active"}
        # circuits
        self.circuits.circuits.default = {"status": "active"}

    def version(self) -> str:
        """Get Netbox status version.

        :return: Netbox version if version >=3.* else "".
        """
        status_d: DAny = self.status.get()
        version = NbBranch(status_d).str("netbox-version")
        return version
