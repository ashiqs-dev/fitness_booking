
🏋️‍♂️ Fitness Booking API

A simple, modular RESTful API built with Flask for managing bookings in a fitness studio. Supports timezone-aware class scheduling, booking validation, and user-specific retrieval.

📦 Features
- 📚 List upcoming fitness classes with optional timezone support
- ✅ Book a spot in a class (with slot validation)
- 📩 Retrieve all bookings by email
- ⏰ Timezone-aware datetime handling (IST by default)
- 🛡️ Duplicate booking prevention
- 📋 Input validation and error handling
- 📝 Centralized logging (daily logs)
- 🧪In-memory DB

🔧 Tech Stack
- Python 3.10+
- Flask 2.3+
- Flask-SQLAlchemy
- SQLite (in-memory)
- Pytz

🚀 Getting Started
1. Clone the repo:
   git clone https://github.com/ashiqs-dev/fitness_booking.git
   cd fitness_booking

2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   python run.py

📘 API Documentation

GET /classes
- List all upcoming classes with optional timezone conversion.
- Query Params: timezone (optional) — e.g., Asia/Tokyo

POST /book
- Book a class by providing:
  {
    "class_id": 1,
    "client_name": "Ashiq",
    "client_email": "ashiq@example.com"
  }

GET /bookings?email=...
- Retrieve all bookings made by a specific email.

📂 Project Structure
fitness_booking_api/
├── app/
│   ├── classes/
│   ├── bookings/
│   ├── models.py
│   ├── database.py
│   ├── seed.py
│   ├── utils.py
│   └── logging_config.py
├── run.py
├── requirements.txt
└── README.md

📁 Logging
Logs are saved in /logs/YYYY-MM-DD.log and also printed to console. They include API hits, warnings, and internal errors.
