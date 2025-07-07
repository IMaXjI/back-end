import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DB_NAME = "recipes.db"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


class Database:
    """Database management interface"""

    _engine = None
    _session = None
    _base = None
    _DB_URL = f"sqlite+aiosqlite:///./{DB_NAME}"

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            cls._engine = create_async_engine(cls._DB_URL, echo=True)
        return cls._engine

    @classmethod
    def get_session(cls):
        if cls._session is None:
            async_session = scoped_session(
                sessionmaker(cls.get_engine(), expire_on_commit=False, class_=AsyncSession)
            )
            cls._session = async_session()
        return cls._session

    @classmethod
    def get_declarative_base(cls):
        if cls._base is None:
            cls._base = declarative_base()
        return cls._base
