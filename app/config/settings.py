# app/config/settings.py
#
# Centralized application configuration.
# All environment variables are loaded once here and reused across the app.
# This avoids scattering "os.getenv(...)" calls in multiple files.

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # General application settings
    app_name: str = "FastAPI Learning Project"
    app_env: str = "development"
    app_debug: bool = True

    # Database connection settings (PostgreSQL)
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_name: str = "fastapi_learning"

    # JWT Settings
    # JWT settings
    secret_key: str =
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    # Tell pydantic where to load environment variables from
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @property
    def database_dsn(self) -> str:
        """Build the PostgreSQL DSN used by asyncpg from individual settings."""
        return (
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


# Single shared instance, imported wherever settings are needed
settings = Settings()
