from sqlalchemy import Column, Integer, String
from database import Base

class Zaposleni(Base):
    __tablename__ = "Zaposleni"
    jmbg = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    account_number = Column(Integer, index=True)

class Patient(Base):
    __tablename__ = "Patients"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    phone_number = Column(Integer, index= True)
 