from pydantic import (
    BaseSettings,
)


class Settings(BaseSettings):
    simple_topic: str = "simple-topic"
    broker_url: str = ""

    class Config:
        env_file = '.env'


settings = Settings()
