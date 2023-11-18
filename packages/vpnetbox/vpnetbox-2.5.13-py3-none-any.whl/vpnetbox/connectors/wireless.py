# pylint: disable=R0902,R0903

"""Wireless Connectors."""

from vpnetbox.connectors.base_c import BaseC


class WirelessCA:
    """Wireless Connectors."""

    def __init__(self, **kwargs):
        """Init WirelessCA."""
        self.wireless_lan_groups = self.WirelessLanGroupsC(**kwargs)
        self.wireless_lans = self.WirelessLansC(**kwargs)
        self.wireless_links = self.WirelessLinksC(**kwargs)

    class WirelessLanGroupsC(BaseC):
        """WirelessLanGroupsC."""

        path = "wireless/wireless-lan-groups/"

    class WirelessLansC(BaseC):
        """WirelessLansC."""

        path = "wireless/wireless-lans/"

    class WirelessLinksC(BaseC):
        """WirelessLinksC."""

        path = "wireless/wireless-links/"
