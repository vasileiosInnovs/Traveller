from app.extensions.database import db

class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    license_number = db.Column(db.String)
    experience_years = db.Column(db.Integer)
    status = db.Column(db.String, default="Available")

    assigned_schedules = db.relationship("Schedule", backref="driver")
