from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://calculator:calculator@localhost:27017/?authSource=calculator&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
db = client['calculator']


class User(BaseModel):
    id: str
    name: str
    username: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }