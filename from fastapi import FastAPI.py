from fastapi import FastAPI

app = FastAPI()

students = []

@app.post("/students")
def add_student(name: str):
    students.append(name)
    return {"message": "Student Added", "students": students}

@app.get("/students")
def get_students():
    return {"students": students}

@app.put("/students")
def update_student(old_name: str, new_name: str):
    if old_name in students:
        index = students.index(old_name)
        students[index] = new_name
        return {"message": "Student Updated"}
    return {"message": "Student Not Found"}

@app.delete("/students")
def delete_student(name: str):
    if name in students:
        students.remove(name)
        return {"message": "Student Deleted"}
    return {"message": "Student Not Found"}

