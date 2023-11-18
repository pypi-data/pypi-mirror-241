# pylint: disable=R0902,R0903

"""Virtualization Connectors."""

from vpnetbox.connectors.base_c import BaseC


class VirtualizationCA:
    """Virtualization Connectors."""

    def __init__(self, **kwargs):
        """Init VirtualizationCA."""
        self.cluster_groups = self.ClusterGroupsC(**kwargs)
        self.cluster_types = self.ClusterTypesC(**kwargs)
        self.clusters = self.ClustersC(**kwargs)
        self.interfaces = self.InterfacesC(**kwargs)
        self.virtual_machines = self.VirtualMachinesC(**kwargs)

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        return f"<{name}: {self.cluster_groups.host}>"

    class ClusterGroupsC(BaseC):
        """ClusterGroupsC."""

        path = "virtualization/cluster-groups/"

    class ClusterTypesC(BaseC):
        """ClusterTypesC."""

        path = "virtualization/cluster-types/"

    class ClustersC(BaseC):
        """ClustersC."""

        path = "virtualization/clusters/"

    class InterfacesC(BaseC):
        """InterfacesC."""

        path = "virtualization/interfaces/"

    class VirtualMachinesC(BaseC):
        """VirtualMachinesC."""

        path = "virtualization/virtual-machines/"
