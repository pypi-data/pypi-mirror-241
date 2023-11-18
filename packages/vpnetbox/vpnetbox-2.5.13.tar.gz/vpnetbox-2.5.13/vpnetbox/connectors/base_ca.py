# pylint: disable=R0902,R0903

"""Base for application Connectors."""

from __future__ import annotations

from vpnetbox import helpers as h


class BaseCA:
    """Base for application Connectors."""

    def __repr__(self) -> str:
        """__repr__."""
        name = self.__class__.__name__
        attrs = h.attr_names(self)
        attr = attrs[0]
        host = getattr(self, attr).host
        return f"<{name}: {host}>"
