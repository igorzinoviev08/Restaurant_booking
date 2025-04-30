from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.reservations import create_reservation, get_reservations, check_reservation_conflict
from ..schemas.reservations import ReservationCreate, ReservationResponse
from ..database import get_db
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/", response_model=list[ReservationResponse])
def read_reservations(db: Session = Depends(get_db)):
    return get_reservations(db)

@router.post("/", response_model=ReservationResponse)
def create_new_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    start_time = reservation.reservation_time
    end_time = start_time + timedelta(minutes=reservation.duration_minutes)

    if check_reservation_conflict(db, reservation.table_id, start_time, end_time):
        raise HTTPException(status_code=400, detail="This table is already reserved for the selected time")

    return create_reservation(db, reservation)