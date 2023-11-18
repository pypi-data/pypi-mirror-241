# pylint: disable=R0902,R0903

"""Circuits Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class CircuitsFA(BaseFA):
    """Circuits Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init CircuitsFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.circuit_terminations = self.CircuitTerminationsF(self)
        self.circuit_types = self.CircuitTypesF(self)
        self.circuits = self.CircuitsF(self)
        self.provider_accounts = self.ProviderAccountsF(self)
        self.provider_networks = self.ProviderNetworksF(self)
        self.providers = self.ProvidersF(self)

    class CircuitTerminationsF(BaseF):
        """CircuitTerminationsF."""

    class CircuitTypesF(BaseF):
        """CircuitTypesF."""

    class CircuitsF(BaseF):
        """CircuitsF."""

    class ProviderAccountsF(BaseF):
        """ProviderAccountsF."""

    class ProviderNetworksF(BaseF):
        """ProviderNetworksF."""

    class ProvidersF(BaseF):
        """ProvidersF."""
