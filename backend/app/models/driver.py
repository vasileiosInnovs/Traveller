from app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Driver(db.Model, SerializerMixin):
    __tablename__ = "drivers"

    serialize_only = ('name', 'phone', 'status',)
    serialize_rules = ('-schedule.driver',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    license_number = db.Column(db.String)
    experience_years = db.Column(db.Integer)
    status = db.Column(db.String, default="Available")

    schedules = db.relationship("Schedule", back_populates="driver")

    