from fastapi import APIRouter
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.core.deps import get_session
from src.schemas.login_schema import LoginSchema
from src.models.cadastro_model import CadastroModel

router = APIRouter()


# secret = 'cf8bd5443187d1fd068b41a63115fe66c5f381a7b27f9d75'
# manager = LoginManager(secret, '/login')


# Post Login

@router.post('/token')
async def login(login_data: LoginSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        senha = login_data.senha
        email = login_data.email
        query = select(CadastroModel.email, CadastroModel.senha).filter(CadastroModel.email == email,
                                                                        CadastroModel.senha == senha)
        result = await session.execute(query)
        usuario: CadastroModel = result.scalars().unique().one_or_none()

        if usuario:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='Login realizado.')

        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Dados de acesso incorretos.')
