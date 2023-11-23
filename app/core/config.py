# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_subscription_key: str
    azure_region: str

    class Config:
        env_file = ".env"

settings = Settings()