from fastapi import Request, APIRouter
from pymongo import mongo_client

db_router = APIRouter()

@db_router.post("/upload_db")
def connect_to_db(request: Request):

    query_params = request.query_params



    return {"result": "successful"}
    

