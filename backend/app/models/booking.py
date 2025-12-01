from app.extensions.database import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

class Booking(db.Model, SerializerMixin):
    __tablename__ = "bookings"

    serialize_only = ('schedule_id', 'user_id', 'seat_id', 'status')
    serialize_rules = ('-user.bookings', '-schedule.bookings', '-seat.booking',)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    schedule_id = db.Column(db.Integer, db.ForeignKey("schedules.id"))
    seat_id = db.Column(db.Integer, db.ForeignKey("seats.id"))
    booking_ref = db.Column(db.String, unique=True)
    payment_status = db.Column(db.String, default="Pending")  # Pending / Paid / Cancelled
    payment_method = db.Column(db.String)
    total_fare = db.Column(db.Float)
    booked_at = db.Column(db.DateTime, default=datetime)
    status = db.Column(db.String, default="Active")  # Active / Cancelled / Completed

    user = db.relationship("User", back_populates="bookings")
    schedule = db.relationship("Schedule", back_populates="bookings")
    seat = db.relationship("Seat", back_populates="booking")