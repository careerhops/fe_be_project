from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()


OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
#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


app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI backend running"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}


# ===============================
# 🤖 LLM Section
# ===============================

@app.get("/ask")
def ask(question: str):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/xml"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return {"error": response.text}

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    return {
        "question": question,
        "answer": answer
    }
