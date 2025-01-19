from fastapi import Request, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient
import os

db_router = APIRouter()

#this comes from the submission
class complete_user_json(BaseModel):
    user_id: str
    user_name: str
    user_upload_time: str
    user_job_position: str
    keyword_metric: str
    sentiment_metric: str
    ats_metric: str

#this comes from login
class userLogin(BaseModel):
    user_name: str
    password: str

    def __hash__(self):
        return hash((self.user_name, self.password))

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

    existing_user = await collection.find_one({"user_id": user_inserted_document["user_id"]}) #note: primary key is now user_id (combo of name and password)
    
    if existing_user:
        raise HTTPException(409, "User already exists!")

    await collection.insert_one(user_dict)

    return {"result": user_inserted_document}

@db_router.post("/generate_user_login")
async def generate_login(user_login: userLogin):
    return {"user_id": hash(userLogin)}

@db_router.post("/retrieve_db_entries")
async def get_db_entries(user : complete_user_json, client: AsyncIOMotorClient = Depends(get_mongo_client)):

    db = client["res_db"]
    collection = db["ResuMaster"]
    # exsiting_user = await collection.find_one({"user_id": })
    

