from app.extensions import db
from sqlalchemy_serializer import SerializerMixin
class Seat(db.Model, SerializerMixin):
    __tablename__ = "seats"
    
    serialize_only = ('bus_id', 'seat_number', 'is_available', 'seat_class',)

    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"))
    seat_number = db.Column(db.String)
    is_available = db.Column(db.Boolean, default=True)
    seat_class = db.Column(db.String)  # Economy / VIP / Sleeper

    bus = db.relationship("Bus", back_populates="seats")
    booking = db.relationship("Booking", back_populates="seat", uselist=False)

    def __repr__(self):
        return f'<Bus ID: {self.bus_id}, Seat Number: {self.seat_number}, Availability: {self.is_available}, Class: {self.seat_class}>'