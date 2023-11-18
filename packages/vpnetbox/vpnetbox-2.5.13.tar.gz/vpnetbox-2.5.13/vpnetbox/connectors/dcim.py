# pylint: disable=R0902,R0903

"""Data Center Infrastructure Connectors."""

from vpnetbox.connectors.base_c import BaseC


class DcimCA:
    """Data Center Infrastructure Connectors."""

    def __init__(self, **kwargs):
        """Init DcimCA."""
        self.cable_terminations = self.CableTerminationsC(**kwargs)
        self.cables = self.CablesC(**kwargs)
        self.connected_device = self.ConnectedDeviceC(**kwargs)
        self.console_port_templates = self.ConsolePortTemplatesC(**kwargs)
        self.console_ports = self.ConsolePortsC(**kwargs)
        self.console_server_port_templates = self.ConsoleServerPortTemplatesC(**kwargs)
        self.console_server_ports = self.ConsoleServerPortsC(**kwargs)
        self.device_bay_templates = self.DeviceBayTemplatesC(**kwargs)
        self.device_bays = self.DeviceBaysC(**kwargs)
        self.device_roles = self.DeviceRolesC(**kwargs)
        self.device_types = self.DeviceTypesC(**kwargs)
        self.devices = self.DevicesC(**kwargs)
        self.front_port_templates = self.FrontPortTemplatesC(**kwargs)
        self.front_ports = self.FrontPortsC(**kwargs)
        self.interface_templates = self.InterfaceTemplatesC(**kwargs)
        self.interfaces = self.InterfacesC(**kwargs)
        self.inventory_item_roles = self.InventoryItemRolesC(**kwargs)
        self.inventory_item_templates = self.InventoryItemTemplatesC(**kwargs)
        self.inventory_items = self.InventoryItemsC(**kwargs)
        self.locations = self.LocationsC(**kwargs)
        self.manufacturers = self.ManufacturersC(**kwargs)
        self.module_bay_templates = self.ModuleBayTemplatesC(**kwargs)
        self.module_bays = self.ModuleBaysC(**kwargs)
        self.module_types = self.ModuleTypesC(**kwargs)
        self.modules = self.ModulesC(**kwargs)
        self.platforms = self.PlatformsC(**kwargs)
        self.power_feeds = self.PowerFeedsC(**kwargs)
        self.power_outlet_templates = self.PowerOutletTemplatesC(**kwargs)
        self.power_outlets = self.PowerOutletsC(**kwargs)
        self.power_panels = self.PowerPanelsC(**kwargs)
        self.power_port_templates = self.PowerPortTemplatesC(**kwargs)
        self.power_ports = self.PowerPortsC(**kwargs)
        self.rack_reservations = self.RackReservationsC(**kwargs)
        self.rack_roles = self.RackRolesC(**kwargs)
        self.racks = self.RacksC(**kwargs)
        self.rear_port_templates = self.RearPortTemplatesC(**kwargs)
        self.rear_ports = self.RearPortsC(**kwargs)
        self.regions = self.RegionsC(**kwargs)
        self.site_groups = self.SiteGroupsC(**kwargs)
        self.sites = self.SitesC(**kwargs)
        self.virtual_chassis = self.VirtualChassisC(**kwargs)
        self.virtual_device_contexts = self.VirtualDeviceContextsC(**kwargs)

    class CableTerminationsC(BaseC):
        """CableTerminationsC."""

        path = "dcim/cable-terminations/"

    class CablesC(BaseC):
        """CablesC."""

        path = "dcim/cables/"

    class ConnectedDeviceC(BaseC):
        """ConnectedDeviceC."""

        path = "dcim/connected-device/"

    class ConsolePortTemplatesC(BaseC):
        """ConsolePortTemplatesC."""

        path = "dcim/console-port-templates/"

    class ConsolePortsC(BaseC):
        """ConsolePortsC."""

        path = "dcim/console-ports/"

    class ConsoleServerPortTemplatesC(BaseC):
        """ConsoleServerPortTemplatesC."""

        path = "dcim/console-server-port-templates/"

    class ConsoleServerPortsC(BaseC):
        """ConsoleServerPortsC."""

        path = "dcim/console-server-ports/"

    class DeviceBayTemplatesC(BaseC):
        """DeviceBayTemplatesC."""

        path = "dcim/device-bay-templates/"

    class DeviceBaysC(BaseC):
        """DeviceBaysC."""

        path = "dcim/device-bays/"

    class DeviceRolesC(BaseC):
        """DeviceRolesC."""

        path = "dcim/device-roles/"

    class DeviceTypesC(BaseC):
        """DeviceTypesC."""

        path = "dcim/device-types/"

    class DevicesC(BaseC):
        """DevicesC."""

        path = "dcim/devices/"

        def __init__(self, **kwargs):
            """Init DevicesC."""
            super().__init__(**kwargs)
            self._parallels.extend([
                "cf_sw_version",
                "has_primary_ip",
                "virtual_chassis_member",
            ])

    class FrontPortTemplatesC(BaseC):
        """FrontPortTemplatesC."""

        path = "dcim/front-port-templates/"

    class FrontPortsC(BaseC):
        """FrontPortsC."""

        path = "dcim/front-ports/"

    class InterfaceTemplatesC(BaseC):
        """InterfaceTemplatesC."""

        path = "dcim/interface-templates/"

    class InterfacesC(BaseC):
        """InterfacesC."""

        path = "dcim/interfaces/"

    class InventoryItemRolesC(BaseC):
        """InventoryItemRolesC."""

        path = "dcim/inventory-item-roles/"

    class InventoryItemTemplatesC(BaseC):
        """InventoryItemTemplatesC."""

        path = "dcim/inventory-item-templates/"

    class InventoryItemsC(BaseC):
        """InventoryItemsC."""

        path = "dcim/inventory-items/"

    class LocationsC(BaseC):
        """LocationsC."""

        path = "dcim/locations/"

    class ManufacturersC(BaseC):
        """ManufacturersC."""

        path = "dcim/manufacturers/"

    class ModuleBayTemplatesC(BaseC):
        """ModuleBayTemplatesC."""

        path = "dcim/module-bay-templates/"

    class ModuleBaysC(BaseC):
        """ModuleBaysC."""

        path = "dcim/module-bays/"

    class ModuleTypesC(BaseC):
        """ModuleTypesC."""

        path = "dcim/module-types/"

    class ModulesC(BaseC):
        """ModulesC."""

        path = "dcim/modules/"

    class PlatformsC(BaseC):
        """PlatformsC."""

        path = "dcim/platforms/"

    class PowerFeedsC(BaseC):
        """PowerFeedsC."""

        path = "dcim/power-feeds/"

    class PowerOutletTemplatesC(BaseC):
        """PowerOutletTemplatesC."""

        path = "dcim/power-outlet-templates/"

    class PowerOutletsC(BaseC):
        """PowerOutletsC."""

        path = "dcim/power-outlets/"

    class PowerPanelsC(BaseC):
        """PowerPanelsC."""

        path = "dcim/power-panels/"

    class PowerPortTemplatesC(BaseC):
        """PowerPortTemplatesC."""

        path = "dcim/power-port-templates/"

    class PowerPortsC(BaseC):
        """PowerPortsC."""

        path = "dcim/power-ports/"

    class RackReservationsC(BaseC):
        """RackReservationsC."""

        path = "dcim/rack-reservations/"

    class RackRolesC(BaseC):
        """RackRolesC."""

        path = "dcim/rack-roles/"

    class RacksC(BaseC):
        """RacksC."""

        path = "dcim/racks/"

    class RearPortTemplatesC(BaseC):
        """RearPortTemplatesC."""

        path = "dcim/rear-port-templates/"

    class RearPortsC(BaseC):
        """RearPortsC."""

        path = "dcim/rear-ports/"

    class RegionsC(BaseC):
        """RegionsC."""

        path = "dcim/regions/"

    class SiteGroupsC(BaseC):
        """SiteGroupsC."""

        path = "dcim/site-groups/"

    class SitesC(BaseC):
        """SitesC."""

        path = "dcim/sites/"

    class VirtualChassisC(BaseC):
        """VirtualChassisC."""

        path = "dcim/virtual-chassis/"

    class VirtualDeviceContextsC(BaseC):
        """VirtualDeviceContextsC."""

        path = "dcim/virtual-device-contexts/"
