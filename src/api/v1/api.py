from fastapi import APIRouter

from src.api.v1.endpoints import cadastro
from src.api.v1.endpoints import login

api_router = APIRouter()
api_router.include_router(cadastro.router, prefix='/cadastro', tags=["Cadastro de usuário"])
api_router.include_router(login.router, prefix='/login', tags=["Login de usuários"])
