from pydantic import BaseModel
from typing import List, Optional

# --------- Pydantic schemas for Musicians ---------

class InstrumentBase(BaseModel):
    name: str

class InstrumentCreate(InstrumentBase):
    pass

class Instrument(InstrumentBase):
    id: int
    musician_id: Optional[int] = None

    class Config:
        orm_mode = True  

class MusicianBase(BaseModel):
    name: str
    address: str

class MusicianCreate(MusicianBase):
    pass

class Musician(MusicianBase):
    id: int
    instruments: List[Instrument] = []

    class Config:
        orm_mode = True  
