from __future__ import annotations

import logging
from typing import Any

from lsrestclient import LsRestClient

log = logging.getLogger(__name__)


# class EventixClientSession(LsRestClient):
#     def __init__(self, base_url: str = None) -> None:
#         self.client = LsRestClient(base_url, name="")
#         self.base_url = base_url
#         super().__init__()
#
#     def request(
#         self,
#         method,
#         url,
#         *args,
#         **kwargs
#     ) -> Response:  # pragma: no cover
#         return requests.request(
#             method,
#             f"{self.base_url}{url}",
#             *args,
#             **kwargs
#         )


def get_client():
    s = LsRestClient(base_url="nohost://", name="eventix_client")
    # s.headers["Connection"] = "close"
    return s


class EventixClient:
    # interface: Any | None = EventixClientSession()
    interface: Any | None = get_client()
    namespace: str | None = None

    @classmethod
    def set_base_url(cls, base_url):
        if isinstance(cls.interface, LsRestClient):
            log.info(f"Setting EventixClient base_url: {base_url}")
            cls.interface.base_url = base_url
