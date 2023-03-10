# Configurações gerais

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    '''
    Classe de configurações gerais usadas na aplicação.
    '''
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:testepostegres@localhost:5432/login"
    DBBaseModel = declarative_base()
    class config:
        case_sesitive = True

settings = Settings()
