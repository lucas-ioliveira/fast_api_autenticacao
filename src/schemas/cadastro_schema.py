from typing import Optional

from pydantic import BaseModel as SCBaseModel


class CadastroSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    sobrenome: str
    email: str
    senha: str

    class Config:
        orm_mode = True
