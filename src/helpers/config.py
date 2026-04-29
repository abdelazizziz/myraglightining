
# pyright: reportCallIssue=false 
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list[str] 
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE:int

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore"
    )

def get_settings():
    return Settings()