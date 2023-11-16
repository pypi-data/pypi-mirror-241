from typing import Literal

from pydantic_settings import BaseSettings


BackendNames = Literal["mongodb", "couchdb"]


class EventixSettings(BaseSettings):
    eventix_backend: BackendNames
