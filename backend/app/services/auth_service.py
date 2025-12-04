import secrets
from datetime import datetime, timedelta

def generate_secure_otp(length=6):
    """Generate a cryptographically secure numeric OTP."""
    return ''.join(secrets.choice("0123456789") for _ in range(length))

def otp_expiry(minutes=5):
    return datetime.utcnow() + timedelta(minutes=minutes)

def verify_otp(stored_otp, stored_expiry, user_input_otp):
    """
    Verify if the OTP is correct and not expired.
    
    Args:
        stored_otp: The OTP stored in the database
        stored_expiry: The expiry datetime stored in the database
        user_input_otp: The OTP entered by the user
    
    Returns:
        tuple: (is_valid, message)
    """
    # Check if OTP has expired
    if datetime.utcnow() > stored_expiry:
        return False, "OTP has expired"
    
    # Check if OTP matches
    if stored_otp != user_input_otp:
        return False, "Invalid OTP"
    
    return True, "OTP verified successfully"