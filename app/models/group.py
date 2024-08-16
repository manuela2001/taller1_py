from pydantic import BaseModel

class Group(BaseModel):
    code:str
    semester:int
    student:Student
    schedule:str
    subject:str