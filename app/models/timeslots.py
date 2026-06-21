from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class TimeSlot(Base):
    __tablename__ = 'time_slot'

    id: Mapped[int] = mapped_column(primary_key=True)
    start_time: Mapped[datetime]
    end_time: Mapped[datetime]
    is_booked : Mapped[bool] = mapped_column(default=False)
    booked_by : Mapped[Optional[str]] = mapped_column(String(30), nullable=True)