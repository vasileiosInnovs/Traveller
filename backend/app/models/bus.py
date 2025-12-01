from app.extensions.database import db

class Bus(db.Model):
    __tablename__ = "buses"

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
