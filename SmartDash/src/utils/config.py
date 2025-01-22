import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))


class Settings(BaseSettings):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/smartdash")

    class Config:
        env_file = ".env"

settings = Settings()
