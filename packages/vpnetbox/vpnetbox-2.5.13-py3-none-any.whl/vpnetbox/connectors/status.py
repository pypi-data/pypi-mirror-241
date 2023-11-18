"""Status Connectors."""

from vpnetbox.connectors.base_c import BaseC
from vpnetbox.types_ import DAny


class StatusC(BaseC):
    """StatusC."""

    path = "status/"

    def get(self, **kwargs) -> DAny:  # type: ignore
        """Get status.

        :return: Dictionary with status data.
        """
        _ = kwargs  # noqa
        return self._get_d()
