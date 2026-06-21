import os
from dotenv import load_dotenv
from typing import AsyncGenerator, Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

load_dotenv()

POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = 5432

DATABASE_URL = \
f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:{POSTGRES_PORT}/{POSTGRES_DB}' 

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

async_sesion_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit = False
)

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sesion_factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]