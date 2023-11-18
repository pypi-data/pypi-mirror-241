# pylint: disable=R0902,R0903

"""Wireless Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class WirelessFA(BaseFA):
    """Wireless Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init WirelessFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.wireless_lan_groups = self.WirelessLanGroupsF(self)
        self.wireless_lans = self.WirelessLansF(self)
        self.wireless_links = self.WirelessLinksF(self)

    class WirelessLanGroupsF(BaseF):
        """WirelessLanGroupsF."""

    class WirelessLansF(BaseF):
        """WirelessLansF."""

    class WirelessLinksF(BaseF):
        """WirelessLinksF."""
