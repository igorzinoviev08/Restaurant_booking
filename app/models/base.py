from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    seats = Column(Integer)
    location = Column(String)

    reservations = relationship("Reservation", back_populates="table")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)

    table = relationship("Table", back_populates="reservations")