from pydantic import (
    BaseSettings,
)


class Settings(BaseSettings):
    TEST: str = 'test2'

    class Config:
        env_file = '.env'


settings = Settings()
