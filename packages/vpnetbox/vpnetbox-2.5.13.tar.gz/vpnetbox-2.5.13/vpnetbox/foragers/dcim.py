# pylint: disable=R0902,R0903

"""DCIM Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class DcimFA(BaseFA):
    """DCIM Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init DcimFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.cable_terminations = self.CableTerminationsF(self)
        self.cables = self.CablesF(self)
        # connected_device, is not model
        self.console_port_templates = self.ConsolePortTemplatesF(self)
        self.console_ports = self.ConsolePortsF(self)
        self.console_server_port_templates = self.ConsoleServerPortTemplatesF(self)
        self.console_server_ports = self.ConsoleServerPortsF(self)
        self.device_bay_templates = self.DeviceBayTemplatesF(self)
        self.device_bays = self.DeviceBaysF(self)
        self.device_roles = self.DeviceRolesF(self)
        self.device_types = self.DeviceTypesF(self)
        self.devices = self.DevicesF(self)
        self.front_port_templates = self.FrontPortTemplatesF(self)
        self.front_ports = self.FrontPortsF(self)
        self.interface_templates = self.InterfaceTemplatesF(self)
        self.interfaces = self.InterfacesF(self)
        self.inventory_item_roles = self.InventoryItemRolesF(self)
        self.inventory_item_templates = self.InventoryItemTemplatesF(self)
        self.inventory_items = self.InventoryItemsF(self)
        self.locations = self.LocationsF(self)
        self.manufacturers = self.ManufacturersF(self)
        self.module_bay_templates = self.ModuleBayTemplatesF(self)
        self.module_bays = self.ModuleBaysF(self)
        self.module_types = self.ModuleTypesF(self)
        self.modules = self.ModulesF(self)
        self.platforms = self.PlatformsF(self)
        self.power_feeds = self.PowerFeedsF(self)
        self.power_outlet_templates = self.PowerOutletTemplatesF(self)
        self.power_outlets = self.PowerOutletsF(self)
        self.power_panels = self.PowerPanelsF(self)
        self.power_port_templates = self.PowerPortTemplatesF(self)
        self.power_ports = self.PowerPortsF(self)
        self.rack_reservations = self.RackReservationsF(self)
        self.rack_roles = self.RackRolesF(self)
        self.racks = self.RacksF(self)
        self.rear_port_templates = self.RearPortTemplatesF(self)
        self.rear_ports = self.RearPortsF(self)
        self.regions = self.RegionsF(self)
        self.site_groups = self.SiteGroupsF(self)
        self.sites = self.SitesF(self)
        self.virtual_chassis = self.VirtualChassisF(self)
        self.virtual_device_contexts = self.VirtualDeviceContextsF(self)

    class CableTerminationsF(BaseF):
        """CableTerminationsF."""

    class CablesF(BaseF):
        """CablesF."""

    class ConsolePortTemplatesF(BaseF):
        """ConsolePortTemplatesF."""

    class ConsolePortsF(BaseF):
        """ConsolePortsF."""

    class ConsoleServerPortTemplatesF(BaseF):
        """ConsoleServerPortTemplatesF."""

    class ConsoleServerPortsF(BaseF):
        """ConsoleServerPortsF."""

    class DeviceBayTemplatesF(BaseF):
        """DeviceBayTemplatesF."""

    class DeviceBaysF(BaseF):
        """DeviceBaysF."""

    class DeviceRolesF(BaseF):
        """DeviceRolesF."""

    class DeviceTypesF(BaseF):
        """DeviceTypesF."""

    class DevicesF(BaseF):
        """DevicesF."""

    class FrontPortTemplatesF(BaseF):
        """FrontPortTemplatesF."""

    class FrontPortsF(BaseF):
        """FrontPortsF."""

    class InterfaceTemplatesF(BaseF):
        """InterfaceTemplatesF."""

    class InterfacesF(BaseF):
        """InterfacesF."""

    class InventoryItemRolesF(BaseF):
        """InventoryItemRolesF."""

    class InventoryItemTemplatesF(BaseF):
        """InventoryItemTemplatesF."""

    class InventoryItemsF(BaseF):
        """InventoryItemsF."""

    class LocationsF(BaseF):
        """LocationsF."""

    class ManufacturersF(BaseF):
        """ManufacturersF."""

    class ModuleBayTemplatesF(BaseF):
        """ModuleBayTemplatesF."""

    class ModuleBaysF(BaseF):
        """ModuleBaysF."""

    class ModuleTypesF(BaseF):
        """ModuleTypesF."""

    class ModulesF(BaseF):
        """ModulesF."""

    class PlatformsF(BaseF):
        """PlatformsF."""

    class PowerFeedsF(BaseF):
        """PowerFeedsF."""

    class PowerOutletTemplatesF(BaseF):
        """PowerOutletTemplatesF."""

    class PowerOutletsF(BaseF):
        """PowerOutletsF."""

    class PowerPanelsF(BaseF):
        """PowerPanelsF."""

    class PowerPortTemplatesF(BaseF):
        """PowerPortTemplatesF."""

    class PowerPortsF(BaseF):
        """PowerPortsF."""

    class RackReservationsF(BaseF):
        """RackReservationsF."""

    class RackRolesF(BaseF):
        """RackRolesF."""

    class RacksF(BaseF):
        """RacksF."""

    class RearPortTemplatesF(BaseF):
        """RearPortTemplatesF."""

    class RearPortsF(BaseF):
        """RearPortsF."""

    class RegionsF(BaseF):
        """RegionsF."""

    class SiteGroupsF(BaseF):
        """SiteGroupsF."""

    class SitesF(BaseF):
        """SitesF."""

    class VirtualChassisF(BaseF):
        """VirtualChassisF."""

    class VirtualDeviceContextsF(BaseF):
        """VirtualDeviceContextsF."""
