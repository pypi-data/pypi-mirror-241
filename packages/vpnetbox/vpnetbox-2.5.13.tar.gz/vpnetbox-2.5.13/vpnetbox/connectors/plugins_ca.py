# pylint: disable=R0902,R0903

"""Plugins Connectors."""

from vpnetbox.connectors.base_c import BaseC
from vpnetbox.types_ import LDAny


class PluginsCA:
    """Plugins Connectors."""

    def __init__(self, **kwargs):
        """Init PluginsCA."""
        self.installed_plugins = self.InstalledPluginsC(**kwargs)

    class InstalledPluginsC(BaseC):
        """InstalledPluginsC."""

        path = "plugins/installed-plugins/"

        def get(self, **kwargs) -> LDAny:
            """Get data."""
            _ = kwargs  # noqa
            return self._get_l()
