import openai
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# ✅ .env file load
load_dotenv()

# ✅ Get API setting val from env
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Check API Key 
if not openai.api_key:
    raise ValueError("❌ OpenAI API Key is missing! check .env file.")

app = FastAPI()

class ChatRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "FastAPI is running! Use /chat to talk to AI."}

@app.post("/chat")
async def chat(request: ChatRequest):
    client = openai.OpenAI()  
    response = client.chat.completions.create(  
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request.query}]
    )
    return {"response": response.choices[0].message.content}
