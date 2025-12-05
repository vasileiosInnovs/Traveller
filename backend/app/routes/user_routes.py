from flask import Blueprint

from app.models import User, Driver

user_bp = Blueprint("user", __name__)

api = Api(user_bp)
#admin
#manager
#customer
#driver  