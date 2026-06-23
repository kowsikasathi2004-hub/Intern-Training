from fastapi import FastAPI

app = FastAPI()

@app.get("/largest")
def largest(a: int, b: int, c: int):
    return {"largest": max(a, b, c)}