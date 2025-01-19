from pydantic import BaseModel
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from database_connection import db_router
from urllib.parse import urlencode, quote_plus
from email.utils import formatdate
from datetime import datetime
import uvicorn
import os
from dotenv import load_dotenv
import httpx
import json 



app = FastAPI()

app.include_router(db_router)

class text_content(BaseModel):
    document_name : str
    type_of_document: str
    job_description: str
    cover_letter: str

class schema_object(BaseModel):
    name: str
    time_of_upload: datetime
    job_position: str
    text_content:text_content


load_dotenv()


def build_url_with_params(base_url, json_obj):
    query_params = urlencode(json_obj, quote_via=quote_plus)
    
    # Construct the full URL by appending the query parameters
    url = f"{base_url}?{query_params}"
    
    return url


@app.post("/upload")
async def process_json_object(response: Response, schema: schema_object):
    chat_response = await ask_chat(job_position=schema.job_position, job_description=schema.text_content.job_description, cover_letter_text=schema.text_content.cover_letter)
    #responds with metrics json
    user_json = {} 
    user_json['user_name'] = schema.name
    user_json['user_upload_time'] = schema.time_of_upload.isoformat()
    user_json['user_job_position'] = schema.job_position

    chat_response_obj = json.loads(chat_response)
    combined_json = json.dumps({ **user_json, **chat_response_obj})
    combined_json_obj = json.loads(combined_json)

    url_with_params = build_url_with_params("/upload_db", json_obj=combined_json_obj)
    return RedirectResponse(url_with_params)



async def ask_chat(job_position: str, job_description: str, cover_letter_text: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": f"Given this job for a {job_position}, identify the keywords in it and compute a percentage ratio of how many keywords I use in my cover letter to the keywords identified in the job description. Now compute a score in percentage format, performing sentiment analysis if the language in my cover letter matches the job description appropriately. Also compute a percentage score for how ATS friendly my cover letter is inferring the ATS will use the job description as its main indicator. Put these results together in a json file with keys: \"key_word_metric\" for the keyword score, \"sentinment_metric\" for the sentiment score,  and \"ats_metric\" for the ats score.  No explanations just give me the json back.\n\n here is the job description: \n{job_description}\n\nand here is the cover letter text: \n{cover_letter_text}\n\n"}]
            }
        )
        message_content = response.json()["choices"][0]["message"]["content"]
        return message_content

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

    




