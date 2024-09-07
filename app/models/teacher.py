from pydantic import BaseModel

class Teacher(BaseModel):
    name:str
    code:str
    subject_id:int
    semester:int