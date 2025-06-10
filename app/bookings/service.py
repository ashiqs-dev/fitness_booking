from app.models import db, Booking, FitnessClass
from app.utils import validate_email
from app.logging_config import logger

def create_booking(data):
    """
    Validates and creates a booking for a fitness class.

    Args:
        data (dict): JSON data containing class_id, client_name, client_email

    Returns:
        tuple: (response JSON, HTTP status code)
    """
    try:
        # Extract booking details from input data
        class_id = data.get("class_id")
        client_name = data.get("client_name")
        client_email = data.get("client_email")

        # Validate that all required fields are present
        if not all([class_id, client_name, client_email]):
            logger.warning("Booking failed due to missing fields.")
            return {"error": "All fields are required."}, 400

        # Validate email format
        if not validate_email(client_email):
            logger.warning(f"Invalid email format: {client_email}")
            return {"error": "Please provide a valid email address."}, 400

        # Check if the fitness class exists
        fitness_class = FitnessClass.query.get(class_id)
        if not fitness_class:
            logger.warning(f"Class with ID {class_id} not found.")
            return {"error": "The class you're trying to book does not exist."}, 404

        # Check if there are available slots in the class
        if fitness_class.available_slots <= 0:
            logger.info(f"Class ID {class_id} is fully booked.")
            return {"error": "Sorry, this class is fully booked."}, 400

        # Check for duplicate booking
        existing_booking = Booking.query.filter_by(
            class_id=class_id,
            client_email=client_email
        ).first()

        if existing_booking:
            logger.warning(f"Duplicate booking attempt by {client_email} for class {class_id}.")
            return {
                "error": "You have already booked this class."
            }, 400
        
        # Create the booking object
        booking = Booking(
            class_id=class_id,
            client_name=client_name,
            client_email=client_email
        )
        # Decrement the available slots for the class
        fitness_class.available_slots -= 1

        # Add the booking to the database session and commit
        db.session.add(booking)
        db.session.commit()

        logger.info(f"Booking successful for {client_email} in class ID {class_id}.")
        return {
            "message": "Booking successful! You have secured your spot.",
            "booking_id": booking.id
        }, 200

    except Exception as error:
        # Log and handle any unexpected errors
        logger.error(f"Booking creation failed: {error}")
        return {"error": "Something went wrong while booking the class. Please try again later."}, 500

def fetch_bookings_by_email(email):
    """
    Fetches all bookings associated with a given client email.

    Args:
        email (str): Email address to search bookings

    Returns:
        tuple: (list of bookings or error message, HTTP status code)
    """
    try:
        # Validate email format
        if not validate_email(email):
            logger.warning(f"Invalid email in fetch: {email}")
            return {"error": "Please provide a valid email address."}, 400

        # Query bookings by client email
        bookings = Booking.query.filter_by(client_email=email).all()
        results = []

        # Format each booking as a dictionary
        for booking in bookings:
            results.append({
                "booking_id": booking.id,
                "class_id": booking.class_id,
                "client_name": booking.client_name,
                "client_email": booking.client_email,
                "timestamp": booking.timestamp.isoformat()
            })

        logger.info(f"Fetched {len(results)} bookings for {email}.")
        return results, 200

    except Exception as error:
        # Log and handle any unexpected errors
        logger.error(f"Failed to retrieve bookings for {email}: {error}")
        return {"error": "Could not fetch bookings at the moment. Please try again."}, 500
