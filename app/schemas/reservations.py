from pydantic import BaseModel
from datetime import datetime

class ReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

class ReservationResponse(BaseModel):
    id: int
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

    class Config:
        orm_mode = True