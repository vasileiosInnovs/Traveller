from app.extensions.database import db
from datetime import datetime
from backports.zoneinfo import ZoneInfo
from sqlalchemy_serializer import SerializerMixin

class Payment(db.Model, SerializerMixin):
    __tablename__ = "payments"

    serialize_only = ('transaction_ref','amount', 'method', 'status',)

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.id"))
    amount = db.Column(db.Float)
    method = db.Column(db.String)
    transaction_ref = db.Column(db.String)
    status = db.Column(db.String, default="Completed")
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Africa/Nairobi")))