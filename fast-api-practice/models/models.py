from pydantic import BaseModel

class Student():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

class Employee(BaseModel):
    name: str
    position: str
    
    def __str__(self):
        return f"Employee(name={self.name}, position={self.position})"