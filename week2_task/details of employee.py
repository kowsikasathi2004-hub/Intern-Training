from fastapi import FastAPI

app = FastAPI()
employees=[]
@app.post("/employee")
def add_employee(salary: int):
    employees.append(salary)
    return {"message": "Employee Added", "employees": employees}
@app.get("/employee")
def get_employees():
    return {"employees": employees}
@app.put("/employee")
def update_employee(old_salary: int, new_salary: int):
    if old_salary in employee:
        index = employees.index(old_salary)
        employees[index] = new_salary
        return {"message": "Employee Updated"}
    return {"message": "Employee Not Found"}
@app.delete("/employees")
def delete_employee(salary: int):
    if salary in employees:
        employees.remove(salary)
        return {"message": "Employee Deleted"}
    return {"message": "Employee Not Found"}
