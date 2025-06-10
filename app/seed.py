from app.models import db, FitnessClass
from datetime import datetime, timedelta
import pytz
from app.logging_config import logger

def seed_fitness_classes():
    """
    Seed the database with initial fitness class data.
    """
    # Clear existing fitness class data
    FitnessClass.query.delete()

    # Set timezone to IST (Asia/Kolkata)
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now()

    # Define fitness class data
    fitness_classes = [
        FitnessClass(
            name="Yoga",
            instructor="Alice",
            datetime=ist_timezone.localize(current_time + timedelta(days=1, hours=9)),
            total_slots=10,
            available_slots=10
        ),
        FitnessClass(
            name="Zumba",
            instructor="Bob",
            datetime=ist_timezone.localize(current_time + timedelta(days=1, hours=11)),
            total_slots=15,
            available_slots=15
        ),
        FitnessClass(
            name="HIIT",
            instructor="Charlie",
            datetime=ist_timezone.localize(current_time + timedelta(days=2, hours=8)),
            total_slots=12,
            available_slots=12
        ),
    ]

    # Add each fitness class to the session
    for fitness_class in fitness_classes:
        db.session.add(fitness_class)

    # Commit the session to save data
    db.session.commit()
    logger.info("Seed data added for fitness classes.")

