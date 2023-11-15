from __future__ import annotations

from typing import Any

from mknodes.basenodes import mknode
from mknodes.utils import log


logger = log.get_logger(__name__)

HTML = '<iframe width="{width}" height="{height}" src="{url}"></iframe>'


class MkIFrame(mknode.MkNode):
    """Node for embedding an IFrame."""

    ICON = "material/web-box"

    def __init__(
        self,
        url: str,
        *,
        width: int = 300,
        height: int = 150,
        **kwargs: Any,
    ):
        """Constructor.

        Arguments:
            url: Url to display in a frame
            width: width of frame in pixels
            height: height of frame in pixels
            kwargs: Keyword arguments passed to parent
        """
        super().__init__(**kwargs)
        self.url = url
        self.width = width
        self.height = height

    def _to_markdown(self) -> str:
        if not self.url:
            return ""
        return HTML.format(url=self.url, width=self.width, height=self.height)


if __name__ == "__main__":
    url = "http://www.google.de"
    # "https://jex.im/regulex/#!embed=true&flags=&re=%5E(a%7Cb)*%3F%24"
    section = MkIFrame(url, header="test")
    print(section)
