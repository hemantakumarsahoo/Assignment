from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Booking API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/classes", response_model=list[schemas.ClassOut])
def read_classes(db: Session = Depends(get_db)):
    return crud.get_classes(db)

@app.post("/book", response_model=schemas.BookingOut)
def book_class(request: schemas.BookingRequest, db: Session = Depends(get_db)):
    booking = crud.create_booking(db, request)
    if not booking:
        raise HTTPException(status_code=400, detail="No slots available or class not found")
    return booking

@app.get("/bookings", response_model=list[schemas.BookingOut])
def get_bookings(email: str, db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)



@app.get("/")
def root():
    return {"message": "Fitness Studio Booking API is running"}
