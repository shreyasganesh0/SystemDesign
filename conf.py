from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Server Application"
    deafult_port: str = "8000"

    model_config = SettingsConfigDict(env_file=".env", extra='allow')
