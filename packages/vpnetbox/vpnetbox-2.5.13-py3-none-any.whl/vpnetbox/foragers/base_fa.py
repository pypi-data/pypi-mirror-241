"""Base for application Foragers."""

from vpnetbox import helpers as h
from vpnetbox.connectors import ConnectorA, NbApi
from vpnetbox.nb_tree import NbTree
from vpnetbox.types_ import LStr


class BaseFA:
    """Base for application Foragers."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init BaseFA.

        :param root: Dictionary where data from Netbox needs to be saved.
        """
        self.api = api
        self.app: str = h.attr_name(self)
        self.root = root
        self.connector: ConnectorA = getattr(api, self.app)  # connector to application

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        count = self.count()
        return f"<{name}: {count}>"

    def count(self) -> int:
        """Count of the Netbox objects in the self root model.

        :return: Count of the Netbox objects.
        """
        return getattr(self.root, self.app).count()

    def get(self, include_nested: bool = True, **kwargs) -> None:
        """Get all objects from Netbox, add objects to root.

        :param include_nested: True - Request base and nested objects,
            False - Request only base objects.
        :param kwargs: Filtering parameters.
        :return: None. Update self root.
        """

        """Get all objects from Netbox, add objects to root.

        :param kwargs: Filtering parameters.
        :return: None. Update self root.
        """
        models: LStr = getattr(self.root, self.app).models()
        for model in models:
            getattr(self, model).get(include_nested=include_nested, **kwargs)
