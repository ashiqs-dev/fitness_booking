# SQLAlchemy models go here
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class FitnessClass(db.Model):
    __tablename__ = 'fitness_class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    instructor = db.Column(db.String(50), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    total_slots = db.Column(db.Integer, nullable=False)
    available_slots = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('fitness_class.id'), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    client_email = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    fitness_class = db.relationship('FitnessClass', backref='bookings')
