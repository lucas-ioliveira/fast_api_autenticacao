from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import Session


# Conexão
async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session

    finally:
        await session.close()
