from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI backend running"}

@app.get("/ask")
def add(a: int, b: int):
    return a+b