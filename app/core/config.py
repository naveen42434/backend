from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AZURE_SUBSCRIPTION_KEY: str = ""
    AZURE_REGION: str
    AZURE_SUBSCRIPTION_ID: str
    AZURE_RESOURCE_GROUP: str

    class Config:
        env_file = ".env"

settings = Settings()