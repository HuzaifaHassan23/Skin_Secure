from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from Security.jwt_tokens import verify_token

security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    
    """Dependency to verify JWT token and extract user information.
    
    Args:
        credentials: HTTP Authorization credentials from request header
    
    Returns:
        Decoded token payload containing user_id, name, email, exp
    
    Raises:
        HTTPException: 401 Unauthorized if token is invalid or expired
    """
    try:
        token = credentials.credentials
        user_data = verify_token(token)
        return user_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
