from pydantic import BaseModel

class Student(BaseModel):
    id:int
    name:str
    code:str
    age:int
    semester:int
    


