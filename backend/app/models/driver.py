from app.extensions import db
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Driver(db.Model, SerializerMixin):
    __tablename__ = "drivers"

    serialize_only = ('name', 'phone', 'status',)
    serialize_rules = ('-schedule.driver',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="driver")
    license_number = db.Column(db.String)
    experience_years = db.Column(db.Integer)
    status = db.Column(db.String, default="Available")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    schedules = db.relationship("Schedule", back_populates="driver")

    