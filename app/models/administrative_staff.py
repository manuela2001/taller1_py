from pydantic import BaseModel

class Administrative_staff(BaseModel):
    id:int
    name:str
    code:str
    gender:str
    dependence:int
