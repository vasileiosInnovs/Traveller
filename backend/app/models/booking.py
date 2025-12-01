from app.extensions.database import db
from datetime import datetime
class Booking(db.Model):
    __tablename__ = "bookings"

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