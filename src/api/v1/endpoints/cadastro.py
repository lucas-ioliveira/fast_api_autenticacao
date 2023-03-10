from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.models.cadastro_model import CadastroModel
from src.schemas.cadastro_schema import CadastroSchema
from src.core.deps import get_session

router = APIRouter()


# Post Cadastro

@router.post('/', response_model=CadastroSchema, status_code=status.HTTP_201_CREATED)
async def post_login(cadastro: CadastroSchema, db: AsyncSession = Depends(get_session)):
    novo_login = CadastroModel(nome=cadastro.nome, sobrenome=cadastro.sobrenome, email=cadastro.email,
                               senha=cadastro.senha)
    db.add(novo_login)
    await db.commit()

    return novo_login


# Get Cadastros


@router.get('/', response_model=List[CadastroSchema])
async def get_logins(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CadastroModel)
        result = await session.execute(query)
        cadastro: List[CadastroModel] = result.scalars().all()

        return cadastro


# Get cadastro


@router.get('/ {cadastro_id}', response_model=CadastroSchema, status_code=status.HTTP_200_OK)
async def get_curso(cadastro_id: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(CadastroModel).filter(CadastroModel.id == cadastro_id)
        result = await sesssion.execute(query)
        cadastro = result.scalar_one_or_none()

        if cadastro:
            return cadastro
        else:
            raise HTTPException(detail='Cadastro não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Put Login


@router.put('/{cadastro_id}', response_model=CadastroSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(cadastro_id: int, login: CadastroSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(CadastroModel).filter(CadastroModel.id == cadastro_id)
        result = await sesssion.execute(query)
        cadastro_up = result.scalar_one_or_none()

        if cadastro_up:
            cadastro_up.nome = login.nome
            cadastro_up.sobrenome = login.sobrenome
            cadastro_up.email = login.email
            cadastro_up.senha = login.senha

            await sesssion.commit()

            return login

        else:
            raise HTTPException(detail='Cadastro não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# Delete Login

@router.delete('/{cadastro_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_login(cadastro_id: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(CadastroModel).filter(CadastroModel.id == cadastro_id)
        result = await sesssion.execute(query)
        cadastro_del = result.scalar_one_or_none()

        if cadastro_del:
            await sesssion.delete(cadastro_del)
            await sesssion.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail='Cadastro não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
