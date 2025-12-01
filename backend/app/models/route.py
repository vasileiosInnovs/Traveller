from app.extensions.database import db

class Route(db.Model):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String)
    destination = db.Column(db.String)
    distance_km = db.Column(db.Float)
    base_fare = db.Column(db.Float)

    buses = db.relationship("Bus", back_populates="route")
    schedules = db.relationship("Schedule", back_populates="route")
