from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/Zaposleni/")
def create_user(name:str, address:str, account_number:int,
                db:Session=Depends(get_db)):
    return crud.create_user(db=db, name=name,
                            address=address, account_number=account_number)

@app.get("/Zaposleni/{user_jmbg}")
def read_user(user_jmbg: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_jmbg=user_jmbg)
    return user

@app.get("/Zaposleni/")
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    print(users)
    return users