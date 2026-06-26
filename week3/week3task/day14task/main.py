from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import TaskCreate, TaskUpdate, TaskResponse
import crud

app = FastAPI()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Task API Working"}


@app.post("/tasks", response_model=TaskResponse)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return  crud.create_task(db, task)


@app.get("/tasks", response_model=list[TaskResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_one(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task Not Found")

    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = crud.update_task(db, task_id, task)

    if updated is None:
        raise HTTPException(status_code=404, detail="Task Not Found")

    return updated


@app.delete("/tasks/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_task(db, task_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Task Not Found")

    return {"message": "Task Deleted Successfully"}
