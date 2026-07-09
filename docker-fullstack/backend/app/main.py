from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "FastAPI Backend Running"}

@app.get("/users")
def users():
    return [
        {"id": 1, "name": "Kowsika"},
        {"id": 2, "name": "Student"}
    ]