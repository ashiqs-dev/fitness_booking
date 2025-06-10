from flask import Blueprint, request, jsonify
from app.bookings.service import create_booking, fetch_bookings_by_email
from app.logging_config import logger

bookings_bp = Blueprint('bookings', __name__)


@bookings_bp.route('/book', methods=['POST'])
def book_class():
    """
    Endpoint to handle booking a fitness class.
    Expects JSON body: { class_id, client_name, client_email }
    Returns success message and booking ID on success.
    """
    try:
        booking_data = request.get_json()
        if not booking_data:
            logger.warning("No JSON body provided in /book request.")
            return jsonify({'error': 'Please provide booking details'}), 400

        response, status = create_booking(booking_data)
        return jsonify(response), status

    except Exception as error:
        logger.error(f"Unhandled error in /book route: {error}")
        return jsonify({'error': 'Something went wrong while processing your booking. Please try again later.'}), 500


@bookings_bp.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to fetch all bookings by a specific email.
    Query parameter: ?email=name@example.com
    """
    try:
        email = request.args.get('email')
        if not email:
            logger.warning("Missing 'email' query parameter in /bookings request.")
            return jsonify({'error': 'Please provide an email address to retrieve bookings.'}), 400

        response, status = fetch_bookings_by_email(email)
        return jsonify(response), status

    except Exception as error:
        logger.error(f"Unhandled error in /bookings route: {error}")
        return jsonify({'error': 'Sorry! We were unable to retrieve your bookings at this time.'}), 500