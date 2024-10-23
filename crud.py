from sqlalchemy.orm import Session
from models import Musician, Instrument


def create_musician(db: Session, name: str, address: str):
    """Create a new musician."""
    musician = Musician(name=name, address=address)
    db.add(musician)
    db.commit()
    db.refresh(musician)
    return musician

def get_musician_by_id(db: Session, musician_id: int):
    """Get a musician by their ID."""
    return db.query(Musician).filter(Musician.id == musician_id).first()

def get_musicians(db: Session, skip: int = 0, limit: int = 10):
    """Get all musicians with pagination."""
    return db.query(Musician).offset(skip).limit(limit).all()

def update_musician(db: Session, musician_id: int, name: str = None, address: str = None):
    """Update an existing musician's details."""
    musician = db.query(Musician).filter(Musician.id == musician_id).first()
    if musician:
        if name:
            musician.name = name
        if address:
            musician.address = address
        db.commit()
        db.refresh(musician)
    return musician

def delete_musician(db: Session, musician_id: int):
    """Delete a musician by their ID."""
    musician = db.query(Musician).filter(Musician.id == musician_id).first()
    if musician:
        db.delete(musician)
        db.commit()
    return musician

# ------------- Instrument CRUD Operations -----------------

def create_instrument(db: Session, name: str, musician_id: int = None):
    """Create a new instrument and associate it with a musician (optional)."""
    instrument = Instrument(name=name, musician_id=musician_id)
    db.add(instrument)
    db.commit()
    db.refresh(instrument)
    return instrument

def get_instrument_by_id(db: Session, instrument_id: int):
    """Get an instrument by its ID."""
    return db.query(Instrument).filter(Instrument.id == instrument_id).first()

def get_instruments(db: Session, skip: int = 0, limit: int = 10):
    """Get all instruments with pagination."""
    return db.query(Instrument).offset(skip).limit(limit).all()

def update_instrument(db: Session, instrument_id: int, name: str = None, musician_id: int = None):
    """Update an existing instrument's details or assign to a musician."""
    instrument = db.query(Instrument).filter(Instrument.id == instrument_id).first()
    if instrument:
        if name:
            instrument.name = name
        if musician_id:
            instrument.musician_id = musician_id
        db.commit()
        db.refresh(instrument)
    return instrument

def delete_instrument(db: Session, instrument_id: int):
    """Delete an instrument by its ID."""
    instrument = db.query(Instrument).filter(Instrument.id == instrument_id).first()
    if instrument:
        db.delete(instrument)
        db.commit()
    return instrument

# ------------- Relationship Operations -----------------

def assign_instrument_to_musician(db: Session, musician_id: int, instrument_id: int):
    """Assign an instrument to a musician (for One-to-Many relationship)."""
    musician = db.query(Musician).filter(Musician.id == musician_id).first()
    instrument = db.query(Instrument).filter(Instrument.id == instrument_id).first()
    
    if musician and instrument:
        instrument.musician_id = musician_id
        db.commit()
        db.refresh(instrument)
    return instrument

def get_musician_instruments(db: Session, musician_id: int):
    """Get all instruments played by a particular musician."""
    musician = db.query(Musician).filter(Musician.id == musician_id).first()
    if musician:
        return musician.instruments
    return []

