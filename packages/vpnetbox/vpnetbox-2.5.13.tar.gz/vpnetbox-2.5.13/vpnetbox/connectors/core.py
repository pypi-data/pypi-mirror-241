# pylint: disable=R0902,R0903

"""Core Connectors."""

from vpnetbox.connectors.base_c import BaseC


class CoreCA:
    """Core Connectors."""

    def __init__(self, **kwargs):
        """Init CoreCA."""
        self.data_files = self.DataFilesC(**kwargs)
        self.data_sources = self.DataSourcesC(**kwargs)
        self.jobs = self.JobsC(**kwargs)

    class DataFilesC(BaseC):
        """DataFilesC."""

        path = "core/data-files/"

    class DataSourcesC(BaseC):
        """DataSourcesC."""

        path = "core/data-sources/"

    class JobsC(BaseC):
        """JobsC."""

        path = "core/jobs/"
