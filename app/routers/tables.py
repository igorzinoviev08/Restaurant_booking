from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..services.tables import create_table, get_tables
from ..schemas.tables import TableCreate, TableResponse
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[TableResponse])
def read_tables(db: Session = Depends(get_db)):
    return get_tables(db)

@router.post("/", response_model=TableResponse)
def create_new_table(table: TableCreate, db: Session = Depends(get_db)):
    return create_table(db, table)