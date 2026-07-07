from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import Task
from schemas import TaskCreate, TaskResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title=task.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(Task).filter(Task.id == task_id).first()


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if db_task:
        db_task.title = task.title
        db.commit()
        db.refresh(db_task)

    return db_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    return {"message": "Task deleted"}