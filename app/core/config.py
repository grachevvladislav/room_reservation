from pydantic import BaseSettings


class Settings(BaseSettings):
    app_author: str
    database_url: str
    path: str
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'Описание'
    database_url: str
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
