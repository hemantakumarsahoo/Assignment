from app.database import SessionLocal, engine, Base
from app.models import FitnessClass
from datetime import datetime, timedelta
import pytz

Base.metadata.create_all(bind=engine)

db = SessionLocal()
db.query(FitnessClass).delete()

tz = pytz.timezone('Asia/Kolkata')
classes = [
    FitnessClass(name="Yoga", datetime=tz.localize(datetime.now() + timedelta(days=1)), instructor="Ram", available_slots=5),
    FitnessClass(name="Zumba", datetime=tz.localize(datetime.now() + timedelta(days=2)), instructor="Rohit", available_slots=10),
    FitnessClass(name="HIIT", datetime=tz.localize(datetime.now() + timedelta(days=3)), instructor="Tanya", available_slots=8),
     FitnessClass(name="Yoga", datetime=tz.localize(datetime.now() + timedelta(days=1)), instructor="Hari", available_slots=4),
]
db.add_all(classes)
db.commit()