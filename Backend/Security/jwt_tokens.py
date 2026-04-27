from datetime import datetime, timedelta
import jwt
from Security.jwt_config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(user_id: int, name: str, email: str) -> str:
    """Create a JWT access token.
    
    Args:
        user_id: The user's ID from database
        name: The user's name
        email: The user's email
    
    Returns:
        Encoded JWT token string
    """
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "exp": expire
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def verify_token(token: str) -> dict:
    """Verify and decode JWT token.
    
    Args:
        token: The JWT token string to verify
    
    Returns:
        Decoded payload dictionary if valid
        
    Raises:
        jwt.ExpiredSignatureError: If token has expired
        jwt.InvalidTokenError: If token is invalid or tampered with
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired, Login again")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
