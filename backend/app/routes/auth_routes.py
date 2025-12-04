
from datetime import datetime
from flask import Blueprint, request
from flask_restful import Api, Resource
from app.extensions.database import db

from app.models.user import User
from app.services.auth_service import generate_secure_otp, otp_expiry

import traceback

from backend.app.extensions.mailer import send_email
from backend.app.models.driver import Driver

auth_bp = Blueprint("auth", __name__)

api = Api(auth_bp)

class SignUp(Resource):
    def post(self):
        try:
            data = request.json

            compulsory_entries = ['username', 'password', 'email']
            if not data or not all(k in data for k in compulsory_entries):
                print('All compulsory entries are not filled')
                return {'error': 'Missing email, password or username'}, 400
            
            if User.query.filter(email=data['email']).first():
                return{'error': 'Email already in use. Please use a different email address.'}, 409

            new_user = User(
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
            data = request.json

            compulsory_entries = ['name', 'password', 'email']
            if not data or not all(k in data for k in compulsory_entries):
                print('All compulsory entries are not filled')
                return {'error': 'Missing email, password or name'}, 400
            
            if User.query.filter(email=data['email']).first():
                return{'error': 'Email already in use. Please use a different email address.'}, 409

            new_driver = Driver(
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
            data = request.json

            if not data or not all(k in data for k in ('email', 'password')):
                return {'error': 'Missing email or password'}, 400
            
            user = User.query.filter(email=data['email']).first()
            if not user:
                print(f"User of email {data.get['email']} does not exist.")
                return {'error': 'Invalid email or password'}, 401
            
            if not user.check_password(data['password']):
                print(f'Incorrect password')
                return {'error': "Invalid email or password"}, 401
            
        except Exception as e:
            print(f"Login error: {str(e)}")
            print(traceback.format_exc())
            return {"error": "Internal server error"}, 500

        
api.add_resource(Login, '/login')

class SendOTP(Resource):
    def post(self):
        try:
            data = request.json

            email = data['email']

            user = User.query.filter(email=email).first()
            if not user:
                return {'error': 'This email is not valid'}, 401
            
            otp = generate_secure_otp()
            expiry = otp_expiry(5)
        
            user.otp_code = otp
            user.otp_expiry = expiry
            db.session.commit()

            html = f"""
            Dear {user.username or user.name},

                <h2>Your Login Verification Code</h2>
                <p>Your 2FA code is:</p>
                <h1>{otp}</h1>
                <p>Expires in 5 minutes.</p>

            """

            send_email(user.email, "Your Verification Code", html)

            return {"message": "OTP sent"}, 200
        
        except Exception as email_error:
            print(f"Failed to send 2FA email: {str(email_error)}")
            return {"error": "Failed to send verification code"}, 500

api.add_resource(SendOTP, '/login/send_otp')

class VerifyOTP(Resource):
    def post(self):
        try:
            data = request.get_json
            
            email = data.get("email")
            otp = data.get("otp")

            user = User.query.filter_by(email=email).first()
            if not user:
                return {"error": "User not found"}, 404
            
            if user.otp_code != otp:
                return {"error": "Invalid OTP"}, 400
            
            if datetime.utcnow() > user.otp_expiry:
                return {"error": "OTP expired"}, 400
            
            token = user.generate_jwt()

            user.otp_code = None
            user.otp_expiry = None
            db.session.commit()

            return {"message": "Login successful", "token": token}, 200
            
        except Exception as e:
            print(f"Failed to verify OTP ")
            return {'error' : 'OTP verification failed'}, 500
        
api.add_resource(VerifyOTP, '/login/verify_otp')