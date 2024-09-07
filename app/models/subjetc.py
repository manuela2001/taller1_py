from pydantic import BaseModel

class Subject(BaseModel):
    name:str
    code:str
    teacher_id:int
    hours:int
    semester:int