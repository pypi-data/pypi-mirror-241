# pylint: disable=R0902,R0903

"""Circuits Connectors."""

from vpnetbox.connectors.base_c import BaseC
from vpnetbox.connectors.base_ca import BaseCA


class CircuitsCA(BaseCA):
    """Circuits Connectors."""

    def __init__(self, **kwargs):
        """Init CircuitsCA."""
        self.circuit_terminations = self.CircuitTerminationsC(**kwargs)
        self.circuit_types = self.CircuitTypesC(**kwargs)
        self.circuits = self.CircuitsC(**kwargs)
        self.provider_accounts = self.ProviderAccountsC(**kwargs)
        self.provider_networks = self.ProviderNetworksC(**kwargs)
        self.providers = self.ProvidersC(**kwargs)

    class CircuitTerminationsC(BaseC):
        """CircuitTerminationsC."""

        path = "circuits/circuit-terminations/"

    class CircuitTypesC(BaseC):
        """CircuitTypesC."""

        path = "circuits/circuit-types/"

    class CircuitsC(BaseC):
        """CircuitsC."""

        path = "circuits/circuits/"

    class ProviderAccountsC(BaseC):
        """ProviderAccountsC."""

        path = "circuits/provider-accounts/"

    class ProviderNetworksC(BaseC):
        """ProviderNetworksC."""

        path = "circuits/provider-networks/"

    class ProvidersC(BaseC):
        """ProvidersC."""

        path = "circuits/providers/"
