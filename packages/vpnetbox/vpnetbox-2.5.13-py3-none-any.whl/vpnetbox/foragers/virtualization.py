# pylint: disable=R0902,R0903

"""Tenancy Virtualization."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class VirtualizationFA(BaseFA):
    """Virtualization Virtualization."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init VirtualizationFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.cluster_groups = self.ClusterGroupsF(self)
        self.cluster_types = self.ClusterTypesF(self)
        self.clusters = self.ClustersF(self)
        self.interfaces = self.InterfacesF(self)
        self.virtual_machines = self.VirtualMachinesF(self)

    class ClusterGroupsF(BaseF):
        """ClusterGroupsF."""

    class ClusterTypesF(BaseF):
        """ClusterTypesF."""

    class ClustersF(BaseF):
        """ClustersF."""

    class InterfacesF(BaseF):
        """InterfacesF."""

    class VirtualMachinesF(BaseF):
        """VirtualMachinesF."""
