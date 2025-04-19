import jwt
import bcrypt
from core.config import settings
def encode_jwt(
        payload: dict, 
        private_key: str = settings.authjwt.private_key_path.read_text(),
        algorithm: str = settings.authjwt.algorithm
        ) -> str:
    
    encoded = jwt.encode(
        payload,
        private_key, 
        algorithm=algorithm
        )
    return encoded


def decode_jwt(
        token: str, 
        public_key: str = settings.authjwt.public_key_path.read_text(),
        algorithms: list = settings.authjwt.algorithm
        ) -> dict:
    decoded = jwt.decode(
        token, 
        public_key, 
        algorithms=algorithms
        )
    return decoded

def hash_password(password: str) -> hash:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def validate_password(
        password: str, 
        hashed_password: bytes
        ) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password)