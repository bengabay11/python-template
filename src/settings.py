from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggingSettings(BaseSettings):
    """Logging-related settings."""

    min_log_level: str = "INFO"
    use_file_handlers: bool = False
    log_file: str | None = None


class AppCoreSettings(BaseSettings):
    """Core application settings."""

    app_name: str = "Python Template"
    environment: str = "Development"
    author: str | None = None


class AppSettings(BaseSettings):
    """
    Application settings loaded from environment and `ini` file.

    `.env` file takes precedence over `ini`.
    """

    core: AppCoreSettings = AppCoreSettings()
    logging: LoggingSettings = LoggingSettings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # Important for deeply nested env vars.
        # Properties should be named as `{SECTION}__{PROPERTY}` in `.env`.
        # For example: `CORE__APP_NAME`.
        env_nested_delimiter="__",
        toml_file="../config/config.toml",
    )


settings = AppSettings()
