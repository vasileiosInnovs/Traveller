
from flask import Blueprint, request
from flask_restful import Api, Resource
from app.extensions.database import db
from werkzeug.security import check_password_hash

from app.models.user import User

import traceback

auth_bp = Blueprint("auth", __name__)

api = Api(auth_bp)

class SignUp(Resource):
    def post(self):
        try:
            data = request.json()

            compulsory_entries = ['username', 'password', 'email']
            if not data or not all(k in data for k in compulsory_entries):
                print('All compulsory entries are not filled')
                return {'error': 'Missing email, password or username'}, 400
            
            if User.query.filter(email=data['email']).first():
                return{'error': 'Email already in use. Please use a different email address.'}, 409

            new_user = SignUp(
                username = request.json['username'],
                email = request.json['email'],
                phone = request.json['phone'],
                role = request.json['role']
            )

            new_user.set_password(request.json['password'])
            db.session.add(new_user)
            db.session.commit()

            return {
                'message': 'New user added successfully.',
                'user': new_user      
            }, 201
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Registration error: {str(e)}")
            print(traceback.format_exc())
            return {"error": "Internal server error"}, 500
    
api.add_resource(SignUp, '/user/signup')

class SignUp_dr(Resource):
    def post(self):
        try:
            data = request.json()

            compulsory_entries = ['name', 'password', 'email']
            if not data or not all(k in data for k in compulsory_entries):
                print('All compulsory entries are not filled')
                return {'error': 'Missing email, password or name'}, 400
            
            if User.query.filter(email=data['email']).first():
                return{'error': 'Email already in use. Please use a different email address.'}, 409

            new_driver = SignUp_dr(
                name = request.json['name'],
                email = request.json['email'],
                phone = request.json['phone'],
                role = request.json['role'],
                license_number = request.json['license_number'],
                experience_years = request.json['experience_years']
            )

            new_driver.set_password(request.json['password'])
            db.session.add(new_driver)
            db.session.commit()

            return {
                'message': 'New driver added successfully.',
                'user': new_driver      
            }, 201
        
        except Exception as e:
            db.session.rollback()
            print(f"❌ Registration error: {str(e)}")
            print(traceback.format_exc())
            return {"error": "Internal server error"}, 500
    
api.add_resource(SignUp_dr, '/driver/signup ')

class Login(Resource):
    def post(self):
        try:
            data = request.json()

            if not data or all(k in data for k in ('email', 'password')):
                return {'error': 'Missing email or password'}, 400
            
            user = User.query.filter(email=data['email']).first()
            if not user:
                print(f'User of email {data.get['email']} does not exist.')
                return {'error': 'Invalid email or password'} 
            
            if not user.check_password(data['password']):
                print(f'Incorrect password')
                return {'error': "Invalid email or password"}
            
        except Exception as e:
            print(f"❌ Login error: {str(e)}")
            print(traceback.format_exc())
            return {"error": "Internal server error"}, 500

        
api.add_resource(Login, '/login')