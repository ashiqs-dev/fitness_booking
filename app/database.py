from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.logging_config import logger

def init_db(app):
    # SQLite in-memory DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    logger.info("Configuring in-memory SQLite database.")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        logger.info("In-memory SQLite DB initialized.")

