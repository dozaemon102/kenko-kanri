from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "mysql+pymysql://sanpo:sanpo@localhost:3306/sanpo_ban"
    tz: str = "Asia/Tokyo"


settings = Settings()
