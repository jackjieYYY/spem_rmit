from typing import Optional
from fastapi import APIRouter, Header
from pydantic import BaseModel
from fastapi import HTTPException, FastAPI, Response, Depends
from uuid import UUID, uuid4
from app.routers import JWTHelper
from app.routers.JWTHelper import PayloadData
from app.routers.helper import SessionData
import app.routers.helper as helper
import time

import datetime
router = APIRouter(
    prefix="/games",
    tags=["games"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def start(token: Optional[str] = Header(None)):
    if token is None:
        data = PayloadData(UserId="123", Username="123", LastGameUTCTime=0, WordleArray=[])
        token = JWTHelper.encoded_jwt(data.dict())
        return {"data" : JWTHelper.decode_jwt(token)}
