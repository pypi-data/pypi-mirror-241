# pylint: disable=R0902,R0903

"""Users Connectors."""

from vpnetbox.connectors.base_c import BaseC
from vpnetbox.types_ import DAny


class UsersCA:
    """Users Connectors."""

    def __init__(self, **kwargs):
        """Init UsersCA."""
        self.config = self.ConfigC(**kwargs)
        self.groups = self.GroupsC(**kwargs)
        self.permissions = self.PermissionsC(**kwargs)
        self.tokens = self.TokensC(**kwargs)
        self.users = self.UsersC(**kwargs)

    class ConfigC(BaseC):
        """ConfigC."""

        path = "users/config/"

        def get(self, **kwargs) -> DAny:  # type: ignore
            """Get data."""
            _ = kwargs  # noqa
            return self._get_d()

    class GroupsC(BaseC):
        """GroupsC."""

        path = "users/groups/"

    class PermissionsC(BaseC):
        """PermissionsC."""

        path = "users/permissions/"

    class TokensC(BaseC):
        """TokensC."""

        path = "users/tokens/"

    class UsersC(BaseC):
        """UsersC."""

        path = "users/users/"
