from app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Route(db.Model, SerializerMixin):
    __tablename__ = "routes"

    serialize_only = ('origin', 'destination', 'distance_km', 'bus_fare',)
    serialize_rules = ('-bus.route', '-schedule.route',)

    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String)
    destination = db.Column(db.String)
    distance_km = db.Column(db.Float)
    bus_fare = db.Column(db.Float)

    buses = db.relationship("Bus", back_populates="route")
    schedules = db.relationship("Schedule", back_populates="route")

    def __repr__(self):
        return f'<Origin: {self.origin}, Destination: {self.destination}, Distance: {self.distance_km}, Fare: {self.bus_fare}>'