from fastapi import Request, APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from datetime import datetime
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import os
import json

db_router = APIRouter()
# USER_NAME = "Michael"
# #this comes from the submission
# class complete_user_json(BaseModel):
#     user_name: str
#     user_upload_time: str
#     user_job_position: str
#     key_word_metric: str
#     sentiment_metric: str
#     ats_metric: str

#     def __hash__(self):
#         return hash((self.user_name, self.password))

class user_name(BaseModel):
    user_name: str

def get_mongo_client():
    CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STR")
    client = AsyncIOMotorClient(CONNECTION_STRING)
    return client

@db_router.post("/upload_db")
async def connect_to_db(request: Request, client: AsyncIOMotorClient = Depends(get_mongo_client)):

    user_inserted_document = request.query_params
    user_dict = dict(user_inserted_document)

    db = client["res_db"]
    collection = db["ResuMaster"]

    # existing_user = await collection.find_one({"user_name": user_inserted_document["user_name"]}) #note: primary key is now user_id (combo of name and password)
    
    # if existing_user:
    #     raise HTTPException(409, "User already exists!")

    await collection.insert_one(user_dict)

    return {"result": user_inserted_document}


def serialize_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

def string_to_datetime(date_string):
    date_format = "%Y-%m-%d %H:%M"
    return datetime.strptime(date_string, date_format)

@db_router.post("/retrieve_db_entries")
async def get_db_entries(user_name: user_name, client: AsyncIOMotorClient = Depends(get_mongo_client)):
    db = client["res_db"]
    collection = db["ResuMaster"]
    users_with_name = await collection.find({"user_name": user_name.user_name}).to_list(None)
    serialized_users = [jsonable_encoder(user, custom_encoder={ObjectId: serialize_objectid}) for user in users_with_name]

    serialized_users.sort(key = lambda user: string_to_datetime(user["user_upload_time"]))

    trimmed_list = [serialized_users[i] for i in range(11 if len(serialized_users) >= 10 else len(serialized_users))]

    final_json = json.dumps(trimmed_list) #changes to json string

    return {"result": final_json}
    
    