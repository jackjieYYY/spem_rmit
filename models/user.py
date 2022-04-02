from pydantic import BaseModel
from mongoengine import *

class User(Document):
    userId = StringField(required=True)
    username = StringField()
    password = StringField()
    lastGameUTCTime = IntField()
    WordleArray = ListField()
    # status = 1 default
    # status = 2 gaming
    # status = 3 finished but faild
    # status = 4 finished and success
    status = IntField()
    word = StringField()

    def getPassword(self):
        return self.__password
    def setPassword(self, password):
        self.__password = password
    def getWord(self):
        return self.__word
    def setWord(self, word):
        self.__word = word

    def to_json_word(self):
        return {
            "userId": self.userId,
            "username": self.username,
            "lastGameUTCTime": self.lastGameUTCTime,
            "WordleArray": self.WordleArray,
            "status": self.status,
            "word": self.word
        }
    def to_json(self):
        return {
            "userId": self.userId,
            "username": self.username,
            "lastGameUTCTime": self.lastGameUTCTime,
            "WordleArray": self.WordleArray,
            "status": self.status,
        }

class charResult(BaseModel):
    # code = -2 means the letter is not in the word
    # code = -1 The word is in this letter but not in the correct position
    # code = 1 The word is in this letter and in the correct position
    letter : str
    code : int