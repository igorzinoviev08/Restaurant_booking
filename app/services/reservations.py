from datetime import timedelta
from sqlalchemy.orm import Session
from ..models.base import Reservation

def check_reservation_conflict(db: Session, table_id: int, start_time: datetime, end_time: datetime):
    return db.query(Reservation).filter(
        Reservation.table_id == table_id,
        Reservation.reservation_time < end_time,
        Reservation.reservation_time + Reservation.duration_minutes * 60 > start_time.timestamp()
    ).first()