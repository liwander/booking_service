import asyncio
# from sqlalchemy import select
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemt.orm import DeclarativeBase
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
    class_=AsycnSession,
    expire_on_commit = False
)