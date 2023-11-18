# pylint: disable=R0902,R0903

"""Users Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class UsersFA(BaseFA):
    """Users Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init UsersFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        # config: is not DiDAny
        self.groups = self.GroupsF(self)
        self.permissions = self.PermissionsF(self)
        self.tokens = self.TokensF(self)
        self.users = self.UsersF(self)

    class ConfigF(BaseF):
        """ConfigF."""

    class GroupsF(BaseF):
        """GroupsF."""

    class PermissionsF(BaseF):
        """PermissionsF."""

    class TokensF(BaseF):
        """TokensF."""

    class UsersF(BaseF):
        """UsersF."""
