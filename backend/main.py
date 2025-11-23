from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class Item(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(item: Item):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a text summarizer."},
                {"role": "user", "content": f"Summarize this:\n{item.text}"}
            ],
            max_tokens=150
        )

        summary = response.choices[0].message.content
        return {"summary": summary}

    except Exception as e:
        return {"error": str(e)}
