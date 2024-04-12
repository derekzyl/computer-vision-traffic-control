from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config.database.index import Base, engine


class Traffic(Base):

    
    __tablename__ = "traffic"
    id:Mapped[str] = mapped_column(primary_key=True)
    x1_vehicles:Mapped[int]
    x2_vehicles:Mapped[int]
    y1_vehicles:Mapped[int]
    
    y2_vehicles:Mapped[int]
    x_green_time:Mapped[int]
    y_green_time:Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(default=func.now())
    
    
Base.metadata.create_all(engine)         