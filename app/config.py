from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Ecomm Backend"
    api_prefix: str = "/api/v1"
    environment: str = "dev"

    class Config:
        env_prefix = "ECOMM_"


settings = Settings()
