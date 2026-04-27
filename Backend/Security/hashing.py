import hashlib
from passlib.context import CryptContext

# Setup the Password Hashing Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Hash password using SHA256 first (to handle >72 chars), then bcrypt."""
    # SHA256 ensures consistent 64-char hash regardless of password length
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    # bcrypt hash the SHA256 hash (always 64 chars, well under 72 byte limit)
    return pwd_context.hash(sha256_hash)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a stored bcrypt hash.
    
    Args:
        plain_password: The password to verify
        hashed_password: The stored bcrypt hash (from database)
    
    Returns:
        True if password matches, False otherwise
    """
    # Validate that stored hash is a string
    if not isinstance(hashed_password, str):
        return False
    
    # Hash the provided password with SHA256
    sha256_hash = hashlib.sha256(plain_password.encode()).hexdigest()
    
    # Verify the SHA256 hash against the stored bcrypt hash
    return pwd_context.verify(sha256_hash, hashed_password)
