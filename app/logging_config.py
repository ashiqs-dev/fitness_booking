import logging
import os
from datetime import datetime

# Ensure the logs directory exists
log_directory = "logs"
os.makedirs(log_directory, exist_ok=True)

# Configure the logger
logger = logging.getLogger("fitness_api")
logger.setLevel(logging.INFO)

# Log file name based on current date
log_filename = datetime.now().strftime("%Y-%m-%d") + ".log"
log_filepath = os.path.join(log_directory, log_filename)

# Create file handler and set level
fh = logging.FileHandler(log_filepath)
fh.setLevel(logging.INFO)

# Create console handler and set level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter and add it to handlers
formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add handlers to the logger if they haven't been added already
if not logger.handlers:
    logger.addHandler(fh)
    logger.addHandler(ch)

# Export this logger for use across the app
__all__ = ["logger"]
