from werkzeug.security import generate_password_hash, check_password_hash

def get_password_hash(password: str) -> str:
    """
    Generate a password hash for the given plain-text password using the
    `Werkzeug` library's built-in `generate_password_hash` function.
    """
    return generate_password_hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Check if a plain-text password matches a given hashed password using the
    `Werkzeug` library's built-in `check_password_hash` function.
    """
    return check_password_hash(hashed_password, plain_password)