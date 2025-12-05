from app.extensions import db
from sqlalchemy_serializer import SerializerMixin

class Bus(db.Model, SerializerMixin):
    __tablename__ = "buses"

    serialize_only = ('name', 'registration_number', 'bus_type', 'total_seats', 'status',)
    serialize_rules = ('-route.buses', '-schedule.bus')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    registration_number = db.Column(db.String, unique=True)
    bus_type = db.Column(db.String)
    model = db.Column(db.String)
    year = db.Column(db.Integer)
    total_seats = db.Column(db.Integer)
    amenities = db.Column(db.JSON)  # {"ac": True, "wifi": False}
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"))
    status = db.Column(db.String, default="Active")  # Active / Maintenance / Retired

    route = db.relationship("Route", back_populates="buses")
    schedules = db.relationship("Schedule", back_populates="bus")

    def __repr__(self):
        return f'<Bus: {self.name}, Registration Number: {self.registration_number}, Bus Type: {self.bus_type} ,Total seats: {self.total_seats}, Status: {self.status}>'