from sqlalchemy.orm import Session
import models

def create_user(db: Session, name: str, address: str, account_number: int):
    db_user = models.Zaposleni(name=name, address=address, account_number=account_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db:Session, user_jmbg:int):
    return db.query(models.Zaposleni).filter(models.Zaposleni.jmbg==user_jmbg).first()

def get_users(db:Session):
    return db.query(models.Zaposleni).all()
