import json
from typing import Optional
from unicodedata import name
from fastapi import APIRouter, Header
from pydantic import BaseModel
from fastapi import HTTPException, FastAPI, Response, Depends
from uuid import UUID, uuid4
from app.routers import JWTHelper
from app.routers.RespHelper import resp_err, resp_ok, resp_ok_code


import time
import uuid
from datetime import datetime

from models.user import User
from utils import words
from pydantic import BaseModel
from mongoengine import *

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

connect(host="mongodb+srv://wordle:rmit2020rmit2020@dba-cluster.3zoy1.mongodb.net/wordle?retryWrites=true&w=majority")


class authuser(BaseModel):
    username:str
    password:str


@router.post("/signup")
async def signup(user: authuser):
    uid = uuid.uuid4().hex
    data = User(userId=uid)
    data.username = user.username
    data.password = user.password # need to hash
    data.WordleArray = []
    data.status = 1
    data.save()
    return resp_ok_code(4,{"data":data.to_json(),"token":JWTHelper.encoded_jwt(data.to_json_word())})

@router.post("/signin")
async def signin(webuser: authuser):
    # if game is finished should return the word
    u = User.objects(username=webuser.username).first()
    if u is None:
        return resp_err(-7, "password\username not match")
    if u.password == webuser.password:
        if u.status == 3 or u.status ==4:
            return resp_ok_code(4,{"data":u.to_json_word(),"token":JWTHelper.encoded_jwt(u.to_json_word())})
        else:
            return resp_ok_code(4,{"data":u.to_json(),"token":JWTHelper.encoded_jwt(u.to_json_word())})
    else:
        return resp_err(-7, "password\username not match")