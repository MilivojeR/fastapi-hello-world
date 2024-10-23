from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Musician(Base): 
    __tablename__ = "musicians"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)

    # Relationship to instruments (One-to-Many)
    instruments = relationship("Instrument", back_populates="musician")

class Instrument(Base):
    __tablename__ = "instruments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # Foreign key pointing to the Musician table
    musician_id = Column(Integer, ForeignKey("musicians.id"))

    # Relationship to the musician (Many-to-One)
    musician = relationship("Musician", back_populates="instruments")
