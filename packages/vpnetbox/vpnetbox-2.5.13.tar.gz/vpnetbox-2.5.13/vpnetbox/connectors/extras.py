# pylint: disable=R0902,R0903

"""Extras Connectors."""

from vpnetbox.connectors.base_c import BaseC


class ExtrasCA:
    """Extras Connectors."""

    def __init__(self, **kwargs):
        """Init ExtrasCA."""
        self.bookmarks = self.BookmarksC(**kwargs)
        self.config_contexts = self.ConfigContextsC(**kwargs)
        self.config_templates = self.ConfigTemplatesC(**kwargs)
        self.content_types = self.ContentTypesC(**kwargs)
        self.custom_field_choice_sets = self.CustomFieldChoiceSetsC(**kwargs)
        self.custom_fields = self.CustomFieldsC(**kwargs)
        self.custom_links = self.CustomLinksC(**kwargs)
        self.export_templates = self.ExportTemplatesC(**kwargs)
        self.image_attachments = self.ImageAttachmentsC(**kwargs)
        self.journal_entries = self.JournalEntriesC(**kwargs)
        self.object_changes = self.ObjectChangesC(**kwargs)
        self.reports = self.ReportsC(**kwargs)
        self.saved_filters = self.SavedFiltersC(**kwargs)
        self.scripts = self.ScriptsC(**kwargs)
        self.tags = self.TagsC(**kwargs)
        self.webhooks = self.WebhooksC(**kwargs)

    class BookmarksC(BaseC):
        """BookmarksC."""

        path = "extras/bookmarks/"

    class ConfigContextsC(BaseC):
        """ConfigContextsC."""

        path = "extras/config-contexts/"

    class ConfigTemplatesC(BaseC):
        """ConfigTemplatesC."""

        path = "extras/config-templates/"

    class ContentTypesC(BaseC):
        """ContentTypesC."""

        path = "extras/content-types/"

        def __init__(self, **kwargs):
            """Init ContentTypesC."""
            super().__init__(**kwargs)
            self._parallels.extend([
                "id",
                "app_label",
                "model",
            ])

    class CustomFieldChoiceSetsC(BaseC):
        """CustomFieldChoiceSetsC."""

        path = "extras/custom-field-choice-sets/"

    class CustomFieldsC(BaseC):
        """CustomFieldsC."""

        path = "extras/custom-fields/"

        def __init__(self, **kwargs):
            """Init CustomFieldsC."""
            super().__init__(**kwargs)
            self._parallels.extend([
                "choice_set",
                "choice_set_id",
                "ui_visibility",
            ])

    class CustomLinksC(BaseC):
        """CustomLinksC."""

        path = "extras/custom-links/"

    class ExportTemplatesC(BaseC):
        """ExportTemplatesC."""

        path = "extras/export-templates/"

    class ImageAttachmentsC(BaseC):
        """ImageAttachmentsC."""

        path = "extras/image-attachments/"

    class JournalEntriesC(BaseC):
        """JournalEntriesC."""

        path = "extras/journal-entries/"

    class ObjectChangesC(BaseC):
        """ObjectChangesC."""

        path = "extras/object-changes/"

    class ReportsC(BaseC):
        """ReportsC."""

        path = "extras/reports/"

    class SavedFiltersC(BaseC):
        """SavedFiltersC."""

        path = "extras/saved-filters/"

    class ScriptsC(BaseC):
        """ScriptsC."""

        path = "extras/scripts/"

    class TagsC(BaseC):
        """TagsC."""

        path = "extras/tags/"

    class WebhooksC(BaseC):
        """WebhooksC."""

        path = "extras/webhooks/"
