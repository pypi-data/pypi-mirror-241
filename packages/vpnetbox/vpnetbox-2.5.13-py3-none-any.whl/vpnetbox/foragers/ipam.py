# pylint: disable=R0902,R0903

"""IPAM Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class IpamFA(BaseFA):
    """IPAM Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init IpamFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.aggregates = self.AggregatesF(self)
        self.asn_ranges = self.AsnRangesF(self)
        self.asns = self.AsnsF(self)
        self.fhrp_group_assignments = self.FhrpGroupAssignmentsF(self)
        self.fhrp_groups = self.FhrpGroupsF(self)
        self.ip_addresses = self.IpAddressesF(self)
        self.ip_ranges = self.IpRangesF(self)
        self.l2vpn_terminations = self.L2vpnTerminationsF(self)
        self.l2vpns = self.L2vpnsF(self)
        self.prefixes = self.PrefixesF(self)
        self.rirs = self.RirsF(self)
        self.roles = self.RolesF(self)
        self.route_targets = self.RouteTargetsF(self)
        self.service_templates = self.ServiceTemplatesF(self)
        self.services = self.ServicesF(self)
        self.vlan_groups = self.VlanGroupsF(self)
        self.vlans = self.VlansF(self)
        self.vrfs = self.VrfsF(self)

    class AggregatesF(BaseF):
        """AggregatesF."""

    class AsnRangesF(BaseF):
        """AsnRangesF."""

    class AsnsF(BaseF):
        """AsnsF."""

    class FhrpGroupAssignmentsF(BaseF):
        """FhrpGroupAssignmentsF."""

    class FhrpGroupsF(BaseF):
        """FhrpGroupsF."""

    class IpAddressesF(BaseF):
        """IpAddressesF."""

    class IpRangesF(BaseF):
        """IpRangesF."""

    class L2vpnTerminationsF(BaseF):
        """L2vpnTerminationsF."""

    class L2vpnsF(BaseF):
        """L2vpnsF."""

    class PrefixesF(BaseF):
        """PrefixesF."""

    class RirsF(BaseF):
        """RirsF."""

    class RolesF(BaseF):
        """RolesF."""

    class RouteTargetsF(BaseF):
        """RouteTargetsF."""

    class ServiceTemplatesF(BaseF):
        """ServiceTemplatesF."""

    class ServicesF(BaseF):
        """ServicesF."""

    class VlanGroupsF(BaseF):
        """VlanGroupsF."""

    class VlansF(BaseF):
        """VlansF."""

    class VrfsF(BaseF):
        """VrfsF."""
