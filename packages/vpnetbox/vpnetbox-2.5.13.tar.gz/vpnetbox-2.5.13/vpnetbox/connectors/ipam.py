# pylint: disable=R0902,R0903

"""IP Addresses Connectors."""
from vpnetbox.connectors.base_c import BaseC


class IpamCA:
    """IP Addresses Connectors."""

    def __init__(self, **kwargs):
        """Init IpamCA."""
        self.aggregates = self.AggregatesC(**kwargs)
        self.asn_ranges = self.AsnRangesC(**kwargs)
        self.asns = self.AsnsC(**kwargs)
        self.fhrp_group_assignments = self.FhrpGroupAssignmentsC(**kwargs)
        self.fhrp_groups = self.FhrpGroupsC(**kwargs)
        self.ip_addresses = self.IpAddressesC(**kwargs)
        self.ip_ranges = self.IpRangesC(**kwargs)
        self.l2vpn_terminations = self.L2vpnTerminationsC(**kwargs)
        self.l2vpns = self.L2vpnsC(**kwargs)
        self.prefixes = self.PrefixesC(**kwargs)
        self.rirs = self.RirsC(**kwargs)
        self.roles = self.RolesC(**kwargs)
        self.route_targets = self.RouteTargetsC(**kwargs)
        self.service_templates = self.ServiceTemplatesC(**kwargs)
        self.services = self.ServicesC(**kwargs)
        self.vlan_groups = self.VlanGroupsC(**kwargs)
        self.vlans = self.VlansC(**kwargs)
        self.vrfs = self.VrfsC(**kwargs)

    class AggregatesC(BaseC):
        """AggregatesC."""

        path = "ipam/aggregates/"

        def __init__(self, **kwargs):
            """Init AggregatesC."""
            super().__init__(**kwargs)
            self._parallels.extend([
                "family",
                "prefix",
            ])

    class AsnRangesC(BaseC):
        """AsnRangesC."""

        path = "ipam/asn-ranges/"

    class AsnsC(BaseC):
        """AsnsC."""

        path = "ipam/asns/"

    class FhrpGroupAssignmentsC(BaseC):
        """FhrpGroupAssignmentsC."""

        path = "ipam/fhrp-group-assignments/"

    class FhrpGroupsC(BaseC):
        """FhrpGroupsC."""

        path = "ipam/fhrp-groups/"

    class IpAddressesC(BaseC):
        """IpAddressesC."""

        path = "ipam/ip-addresses/"

        def __init__(self, **kwargs):
            """Init IpAddressesC."""
            super().__init__(**kwargs)
            self._parallels.extend([
                "assigned_to_interface",
                "family",
                "mask_length",
                "parent",
            ])

    class IpRangesC(BaseC):
        """IpRangesC."""

        path = "ipam/ip-ranges/"

    class L2vpnTerminationsC(BaseC):
        """L2vpnTerminationsC."""

        path = "ipam/l2vpn-terminations/"

    class L2vpnsC(BaseC):
        """L2vpnsC."""

        path = "ipam/l2vpns/"

    class PrefixesC(BaseC):
        """PrefixesC."""

        path = "ipam/prefixes/"

        def __init__(self, **kwargs):
            """Init PrefixesC."""
            super().__init__(**kwargs)
            self._parallels.extend([
                "assigned_to_interface",
                "cf_env",
                "family",
                "mask_length",
                "prefix",
            ])

    class RirsC(BaseC):
        """RirsC."""

        path = "ipam/rirs/"

    class RolesC(BaseC):
        """RolesC."""

        path = "ipam/roles/"

    class RouteTargetsC(BaseC):
        """RouteTargetsC."""

        path = "ipam/route-targets/"

    class ServiceTemplatesC(BaseC):
        """ServiceTemplatesC."""

        path = "ipam/service-templates/"

    class ServicesC(BaseC):
        """ServicesC."""

        path = "ipam/services/"

    class VlanGroupsC(BaseC):
        """VlanGroupsC."""

        path = "ipam/vlan-groups/"

    class VlansC(BaseC):
        """VlansC."""

        path = "ipam/vlans/"

    class VrfsC(BaseC):
        """VrfsC."""

        path = "ipam/vrfs/"
