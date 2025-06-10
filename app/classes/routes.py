from flask import Blueprint, jsonify, request
from app.classes.service import get_class_list_response
from app.logging_config import logger

classes_bp = Blueprint('classes', __name__, url_prefix='/classes')


@classes_bp.route('/', methods=['GET'])
def list_classes():
    """
    API endpoint to retrieve all available fitness classes.
    Converts datetime from IST to the requested timezone (defaults to Asia/Kolkata).
    Delegates processing to the service layer.
    """
    try:
        timezone_arg = request.args.get('timezone', 'Asia/Kolkata')
        response, status = get_class_list_response(timezone_arg)
        return jsonify(response), status
    except Exception as error:
        logger.error(f"Unhandled error in /classes route: {error}")
        return jsonify({'error': 'Unexpected server error'}), 500