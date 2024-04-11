from datetime import datetime

from sqlalchemy import create_engine, func
from sqlalchemy.engine import Engine
from sqlalchemy.orm import (DeclarativeBase, Mapped, Session, mapped_column,
                            sessionmaker)

from config.config import Config


def get_config():
  
    return Config()



engine:Engine = create_engine("postgres://zyhaxiam:EHNQbkPk_-lPNqo8dLb3hV40blIvU9sN@stampy.db.elephantsql.com/zyhaxiam")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TimeStamp:
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now())


