from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
from pytz import timezone

def get_classes(db: Session):
    return db.query(models.FitnessClass).filter(models.FitnessClass.datetime >= datetime.now()).all()

def create_booking(db: Session, request: schemas.BookingRequest):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == request.class_id).first()
    if not fitness_class or fitness_class.available_slots <= 0:
        return None
    fitness_class.available_slots -= 1
    booking = models.Booking(**request.dict())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()