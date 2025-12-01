from app.extensions.database import db
class Schedule(db.Model):
    __tablename__ = "schedules"

    id = db.Column(db.Integer, primary_key=True)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"))
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))
    departure_time = db.Column(db.Time)
    arrival_time = db.Column(db.Time)
    travel_date = db.Column(db.Date)
    frequency = db.Column(db.String)  # Daily / Weekly / One-time
    status = db.Column(db.String, default="Scheduled")  # Scheduled / Cancelled / Completed

    bus = db.relationship("Bus", back_populates="schedules")
    route = db.relationship("Route", back_populates="schedules")
    bookings = db.relationship("Booking", back_populates="schedule")