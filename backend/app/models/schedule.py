from app.extensions import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from backports.zoneinfo import ZoneInfo

class Schedule(db.Model, SerializerMixin):
    __tablename__ = "schedules"

    serialize_only = ('bus_id', 'route_id', 'departure_time', 'arrival_time', 'travel_date', 'status',)
    serialize_rules = ('-bus.schedules', '-route.schedules', '-booking.schedule')

    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"))
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))
    departure_time = db.Column(db.DateTime)
    arrival_time = db.Column(db.DateTime)
    travel_date = db.Column(db.Date)
    frequency = db.Column(db.String)  # Daily / Weekly / One-time
    status = db.Column(db.String, default="Scheduled")  # Scheduled / Cancelled / Completed

    bus = db.relationship("Bus", back_populates="schedules")
    route = db.relationship("Route", back_populates="schedules")
    bookings = db.relationship("Booking", back_populates="schedule")
    driver = db.relationship("Driver", back_populates="schedules")

    def __repr__(self):
        return f'<Bus ID: {self.bus_id}, Route ID: {self.route_id}, Departure: {self.departure_time}, Arrival: {self.arrival_time}, Travel Date: {self.travel_date}, Status: {self.status}>'