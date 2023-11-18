# pylint: disable=R0902,R0903

"""Extras Forager."""
from vpnetbox.connectors import NbApi
from vpnetbox.foragers.base_f import BaseF
from vpnetbox.foragers.base_fa import BaseFA
from vpnetbox.nb_tree import NbTree


class ExtrasFA(BaseFA):
    """Extras Forager."""

    def __init__(self, root: NbTree, api: NbApi):
        """Init ExtrasFA.

        :param root: NbTree object where data from Netbox needs to be saved.
        :param api: NbApi object, connector to Netbox API.
        """
        super().__init__(root, api)
        self.bookmarks = self.BookmarksF(self)
        self.config_contexts = self.ConfigContextsF(self)
        self.config_templates = self.ConfigTemplatesF(self)
        self.content_types = self.ContentTypesF(self)
        self.custom_field_choice_sets = self.CustomFieldChoiceSetsF(self)
        self.custom_fields = self.CustomFieldsF(self)
        self.custom_links = self.CustomLinksF(self)
        self.export_templates = self.ExportTemplatesF(self)
        self.image_attachments = self.ImageAttachmentsF(self)
        self.journal_entries = self.JournalEntriesF(self)
        self.object_changes = self.ObjectChangesF(self)
        self.reports = self.ReportsF(self)
        self.saved_filters = self.SavedFiltersF(self)
        self.scripts = self.ScriptsF(self)
        self.tags = self.TagsF(self)
        self.webhooks = self.WebhooksF(self)

    class BookmarksF(BaseF):
        """BookmarksF."""

    class ConfigContextsF(BaseF):
        """ConfigContextsF."""

    class ConfigTemplatesF(BaseF):
        """ConfigTemplatesF."""

    class ContentTypesF(BaseF):
        """ContentTypesF."""

    class CustomFieldChoiceSetsF(BaseF):
        """CustomFieldChoiceSetsF."""

    class CustomFieldsF(BaseF):
        """CustomFieldsF."""

    class CustomLinksF(BaseF):
        """CustomLinksF."""

    class ExportTemplatesF(BaseF):
        """ExportTemplatesF."""

    class ImageAttachmentsF(BaseF):
        """ImageAttachmentsF."""

    class JournalEntriesF(BaseF):
        """JournalEntriesF."""

    class ObjectChangesF(BaseF):
        """ObjectChangesF."""

    class ReportsF(BaseF):
        """ReportsF."""

    class SavedFiltersF(BaseF):
        """SavedFiltersF."""

    class ScriptsF(BaseF):
        """ScriptsF."""

    class TagsF(BaseF):
        """TagsF."""

    class WebhooksF(BaseF):
        """WebhooksF."""
