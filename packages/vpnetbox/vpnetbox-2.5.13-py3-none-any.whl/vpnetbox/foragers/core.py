# pylint: disable=R0902,R0903

"""Core Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class CoreFA(BaseFA):
    """Core Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init CoreFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.data_files = self.DataFilesF(self)
        self.data_sources = self.DataSourcesF(self)
        self.jobs = self.JobsF(self)

    class DataFilesF(BaseF):
        """DataFilesF."""

    class DataSourcesF(BaseF):
        """DataSourcesF."""

    class JobsF(BaseF):
        """JobsF."""
