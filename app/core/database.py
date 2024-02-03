from app import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, Session


DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.SERVER}:{settings.PORT}/{settings.DB_NAME}"

async_engine = create_async_engine(DATABASE_URL, future=True)

async_session = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with async_engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)    
        
        
async def get_session() -> Session:
    async with async_session() as session:
        yield session
