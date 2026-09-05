from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, PostgresDsn
from sqlalchemy.engine import make_url
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    APP_NAME: str = "Brain-Store-API"
    APP_STAGE: str = Field(default='development', min_length=3, max_length=20)
    API_ORIGIN: str = Field(default=..., min_length=6)
    DATABASE_URL: PostgresDsn = Field(default=...)
    PINECONE_API_KEY: str = Field(default=...)
    PINECONE_INDEX_HOST: str = Field(default=...)
    PINECONE_INDEX_NAME: str = Field(default='brain-strore-index')
    GEMINI_API_KEY: str = Field(default=...)

    @property
    def is_production(self) -> bool:
        return self.APP_STAGE == 'production'

    @property
    def async_database_url(self) -> str:
        return str(make_url(str(self.DATABASE_URL)).set(drivername="postgresql+asyncpg", query={}))

    model_config = SettingsConfigDict(
        env_file=f"{base_dir}/.env",
        env_file_encoding='utf-8',
        extra='ignore',
        env_ignore_empty=True
    )


settings = Settings()
