from uuid import UUID
from enum import Enum
from typing import Tuple, Type

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
    PydanticBaseSettingsSource,
)


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class ClientConfig(BaseSettings):
    api_url: str | None = None
    api_key_id: UUID | None = None
    api_key_secret: str | None = None
    api_endpoint_prefix: str = ""
    pretty: bool = False
    verbose: bool = False
    dry_run: bool = False
    retry_count: int = 5
    retry_delay: int = 5
    retry_aggressive: bool = False
    additional_headers: dict[str, str] = {}

    model_config = SettingsConfigDict(
        env_file=(".env.default", ".env", ".env.local", ".env.dev", ".env.prod"),
        env_prefix="LQS_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )
