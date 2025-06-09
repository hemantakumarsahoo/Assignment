# Fitness Booking API

## Setup Instructions

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python seed_data.py
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /classes` — View all upcoming classes
- `POST /book` — Book a class (class_id, client_name, client_email)
- `GET /bookings?email=` — View bookings by email