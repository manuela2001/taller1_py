from pydantic import BaseModel

class Subject(BaseModel):
    code:str
    teacher:Teacher
    student:Student
    hours:int
    semester:int