from typing import Optional
import jwt
from pydantic import BaseModel

secret_key = "RMIT_SEPM!@#$%^&*()_+"

class PayloadData(BaseModel):
    UserId : str
    Username: Optional[str] = None
    LastGameUTCTime: int
    WordleArray: list



def encoded_jwt(payload : PayloadData):
    return jwt.encode(payload, secret_key, algorithm='HS256')

def decode_jwt(token):
    return jwt.decode(token, secret_key, algorithms=['HS256'])