from app.extensions.database import db
class Seat(db.Model):
    __tablename__ = "seats"

    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"))
    seat_number = db.Column(db.String)
    is_available = db.Column(db.Boolean, default=True)
    seat_class = db.Column(db.String)  # Economy / VIP / Sleeper

    bus = db.relationship("Bus", back_populates="seats")
    booking = db.relationship("Booking", back_populates="seat", uselist=False)