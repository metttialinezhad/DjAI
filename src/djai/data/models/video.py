"""DjAI Video DataSet class."""


import sys
if sys.version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence

from .base import _FileDataSetABC


__all__: Sequence[str] = ('VideoDataSet',)


class VideoDataSet(_FileDataSetABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """DjAI Video DataSet class."""

    class Meta(_FileDataSetABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        abstract = True
