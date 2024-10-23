from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from models import Musician, Instrument
from crud import (create_musician, get_musician_by_id, get_musicians, update_musician, delete_musician,
                  create_instrument, get_instruments, assign_instrument_to_musician)
from database import SessionLocal, engine
import models
import schemas  


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------- Musician Endpoints --------

@app.post("/musicians/", response_model=schemas.Musician)
def create_new_musician(musician: schemas.MusicianCreate, db: Session = Depends(get_db)):
    return create_musician(db=db, name=musician.name, address=musician.address)

@app.get("/musicians/{musician_id}", response_model=schemas.Musician)
def read_musician(musician_id: int, db: Session = Depends(get_db)):
    musician = get_musician_by_id(db, musician_id=musician_id)
    if musician is None:
        raise HTTPException(status_code=404, detail="Musician not found")
    return musician

@app.get("/musicians/", response_model=List[schemas.Musician])
def read_musicians(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_musicians(db, skip=skip, limit=limit)

@app.put("/musicians/{musician_id}", response_model=schemas.Musician)
def update_existing_musician(musician_id: int, musician: schemas.MusicianCreate, db: Session = Depends(get_db)):
    updated_musician = update_musician(db, musician_id=musician_id, name=musician.name, address=musician.address)
    if updated_musician is None:
        raise HTTPException(status_code=404, detail="Musician not found")
    return updated_musician

@app.delete("/musicians/{musician_id}", response_model=schemas.Musician)
def delete_existing_musician(musician_id: int, db: Session = Depends(get_db)):
    musician = delete_musician(db, musician_id=musician_id)
    if musician is None:
        raise HTTPException(status_code=404, detail="Musician not found")
    return musician

# -------- Instrument Endpoints --------

@app.post("/instruments/", response_model=schemas.Instrument)
def create_new_instrument(instrument: schemas.InstrumentCreate, musician_id: int = None, db: Session = Depends(get_db)):
    return create_instrument(db=db, name=instrument.name, musician_id=musician_id)

@app.get("/instruments/", response_model=List[schemas.Instrument])
def read_instruments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_instruments(db=db, skip=skip, limit=limit)

@app.put("/musicians/{musician_id}/instruments/{instrument_id}", response_model=schemas.Instrument)
def assign_instrument(musician_id: int, instrument_id: int, db: Session = Depends(get_db)):
    instrument = assign_instrument_to_musician(db=db, musician_id=musician_id, instrument_id=instrument_id)
    if instrument is None:
        raise HTTPException(status_code=404, detail="Instrument or Musician not found")
    return instrument
