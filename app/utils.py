from pytz import timezone, UnknownTimeZoneError
from app.logging_config import logger
import re


def get_timezone(tz_string: str):
    """
    Safely parse the given timezone string into a pytz timezone object.

    Args:
        tz_string (str): Timezone name (e.g., 'Asia/Kolkata')

    Returns:
        pytz.timezone: Parsed timezone object (defaults to Asia/Kolkata on error)
    """
    try:
        tz = timezone(tz_string)
        logger.info(f"Parsed timezone: {tz_string}")
        return tz
    except UnknownTimeZoneError:
        logger.warning(f"Invalid timezone '{tz_string}' received. Defaulting to Asia/Kolkata.")
        return timezone('Asia/Kolkata')

def validate_email(email: str) -> bool:
    """
    Validates an email address using a regex pattern.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    if re.match(pattern, email):
        logger.debug(f"Validated email: {email}")
        return True
    else:
        logger.debug(f"Invalid email format: {email}")
        return False