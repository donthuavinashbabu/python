import uvicorn

from fastapi import FastAPI
from models.models import Student, Employee

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students")
async def student():    
    student = Student(name="John Doe", age=20)
    return {"student": str(student)}

@app.get("/employees", response_model=Employee)
def employee() -> Employee:
    employee = Employee(name="Jane Smith", position="Software Engineer")
    return employee


@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee) -> Employee:
    return employee

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)