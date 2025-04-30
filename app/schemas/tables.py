from pydantic import BaseModel

class TableCreate(BaseModel):
    name: str
    seats: int
    location: str

class TableResponse(BaseModel):
    id: int
    name: str
    seats: int
    location: str

    class Config:
        orm_mode = True