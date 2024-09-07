from pydantic import BaseModel

class Group(BaseModel):
    code:str
    semester:int
    student_id:int
    schedule:str
    subject_id:int