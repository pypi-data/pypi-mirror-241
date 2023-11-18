# pylint: disable=R0902,R0903

"""Tenancy Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class TenancyFA(BaseFA):
    """Tenancy Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init TenancyFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.contact_assignments = self.ContactAssignmentsF(self)
        self.contact_groups = self.ContactGroupsF(self)
        self.contact_roles = self.ContactRolesF(self)
        self.contacts = self.ContactsF(self)
        self.tenant_groups = self.TenantGroupsF(self)
        self.tenants = self.TenantsF(self)

    class TenancyF(BaseF):
        """TenancyF."""

    class ContactAssignmentsF(BaseF):
        """ContactAssignmentsF."""

    class ContactGroupsF(BaseF):
        """ContactGroupsF."""

    class ContactRolesF(BaseF):
        """ContactRolesF."""

    class ContactsF(BaseF):
        """ContactsF."""

    class TenantGroupsF(BaseF):
        """TenantGroupsF."""

    class TenantsF(BaseF):
        """TenantsF."""
