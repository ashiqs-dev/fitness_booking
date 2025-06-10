from flask import Flask
from app.database import init_db
from app.models import db
from app.seed import seed_fitness_classes

from app.classes.routes import classes_bp
from app.bookings.routes import bookings_bp

def create_app():
    app = Flask(__name__)
    init_db(app)

    app.register_blueprint(classes_bp)
    app.register_blueprint(bookings_bp)

    @app.route('/')
    def index():
        return {"message": "Welcome to the Fitness Booking API"}

    with app.app_context():
        seed_fitness_classes()

    return app

# Entry point
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
