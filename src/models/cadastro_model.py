from src.core.configs import settings

from sqlalchemy import Column, Integer, String


class CadastroModel(settings.DBBaseModel):
    __tablename__ = 'login'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    sobrenome: str = Column(String(100))
    email: str = Column(String(100))
    senha: str = Column(String(100))
