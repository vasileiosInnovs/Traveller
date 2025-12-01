from app.extensions.database import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"))
    amount = db.Column(db.Float)
    method = db.Column(db.String)
    transaction_ref = db.Column(db.String)
    status = db.Column(db.String, default="Completed")
    created_at = db.Column(db.DateTime, default=datetime)