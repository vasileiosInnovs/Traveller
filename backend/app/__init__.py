from flask import Flask
from flask_migrate import Migrate
from app.extensions.database import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']

    db.init_app(app)
    migrate.init_app(app, db)

    return app
