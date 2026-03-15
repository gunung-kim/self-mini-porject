from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

class Settings(BaseSettings):
    PROJECT_NAME :str
    VERSION :str="1.0.0"
    DEBUG:bool=True
    DATABASE_URL : str

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore"
    )

print(f"BASE_DIR{BASE_DIR}")
print(f"ENV_PATH{ENV_PATH}")
    
settings = Settings()

