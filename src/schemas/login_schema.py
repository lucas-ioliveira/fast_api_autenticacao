from pydantic import BaseModel as SCBaseModel

class LoginSchema(SCBaseModel):
    email: str
    senha: str
