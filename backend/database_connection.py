from fastapi import Request, APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient
import os

db_router = APIRouter()

class user(BaseModel):
    user_name: str
    user_upload_time: datetime
    user_job_position: str
    keyword_metric: str
    sentiment_metric: str
    ats_metric: str

def get_mongo_client():
    CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STR")
    client = AsyncIOMotorClient(CONNECTION_STRING)
    return client

@db_router.post("/upload_db")
async def connect_to_db(request: Request, client: AsyncIOMotorClient = Depends(get_mongo_client)):

    user_inserted_document = request.query_params
    user_dict = dict(user_inserted_document)


    print("entered try")
    db = client["res_db"]
    collection = db["ResuMaster"]

    print("before find_one")
    existing_user = await collection.find_one({"user_upload_time": user_inserted_document["user_upload_time"]}) #note: primary key is time_uploaded. this screws up if two people add with the same time
    
    
    if existing_user:
        raise HTTPException(409, "User already exists!")

    print("before insert")
    await collection.insert_one(user_dict)
    print("after insert")

    return {"result": user_inserted_document}

@db_router.post("/retrieve_db_entries")
async def get_db_entries(request: Request, client: AsyncIOMotorClient = Depends(get_mongo_client)):

    db = client["res_db"]
    collection = db["ResuMaster"]
    exsiting_user = await collection.find_one()
    

