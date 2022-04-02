import imp
from fastapi import FastAPI
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.session_verifier import SessionVerifier
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from pydantic import BaseModel
from fastapi import HTTPException, FastAPI, Response, Depends
from uuid import UUID, uuid4

import uvicorn
import utils.words as words
from fastapi import Depends, FastAPI

from app.routers import games, user

app = FastAPI()

app.include_router(games.router)
app.include_router(user.router)
@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    words.load_words()
    words.dictTest()
    uvicorn.run(app, host="0.0.0.0", port=8000)