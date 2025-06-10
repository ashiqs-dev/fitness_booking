from app.models import FitnessClass, db
from app.utils import get_timezone
from app.logging_config import logger


def get_class_list_response(timezone_str: str):
    """
    Retrieve and format a list of fitness classes,
    converting class datetimes to the specified timezone.

    Args:
        timezone_str (str): Name of the target timezone (e.g., 'Asia/Kolkata')

    Returns:
        tuple: (List of classes as dicts, HTTP status code)
    """
    try:
        # Get a valid timezone object
        target_timezone = get_timezone(timezone_str)

        # Query classes from database
        logger.info("Fetching fitness classes from database.")
        classes = FitnessClass.query.order_by(FitnessClass.datetime).all()

        # Prepare response data
        response = []
        for fitness_class in classes:
            converted_time = fitness_class.datetime.astimezone(target_timezone)
            response.append({
                'id': fitness_class.id,
                'name': fitness_class.name,
                'instructor': fitness_class.instructor,
                'datetime': converted_time.isoformat(),
                'available_slots': fitness_class.available_slots
            })

        logger.info("Successfully formatted class data for response.")
        return response, 200

    except Exception as error:
        logger.error(f"Failed to prepare class list response: {error}")
        return {'error': 'Unable to fetch class data.'}, 500
