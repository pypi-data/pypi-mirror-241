# pylint: disable=R0902,R0903

"""Tenancy Connectors."""

from vpnetbox.connectors.base_c import BaseC


class TenancyCA:
    """Tenancy Connectors."""

    def __init__(self, **kwargs):
        """Init TenancyCA."""
        self.contact_assignments = self.ContactAssignmentsC(**kwargs)
        self.contact_groups = self.ContactGroupsC(**kwargs)
        self.contact_roles = self.ContactRolesC(**kwargs)
        self.contacts = self.ContactsC(**kwargs)
        self.tenant_groups = self.TenantGroupsC(**kwargs)
        self.tenants = self.TenantsC(**kwargs)

    class ContactAssignmentsC(BaseC):
        """ContactAssignmentsC."""

        path = "tenancy/contact-assignments/"

    class ContactGroupsC(BaseC):
        """ContactGroupsC."""

        path = "tenancy/contact-groups/"

    class ContactRolesC(BaseC):
        """ContactRolesC."""

        path = "tenancy/contact-roles/"

    class ContactsC(BaseC):
        """ContactsC."""

        path = "tenancy/contacts/"

    class TenantGroupsC(BaseC):
        """TenantGroupsC."""

        path = "tenancy/tenant-groups/"

    class TenantsC(BaseC):
        """TenantsC."""

        path = "tenancy/tenants/"
