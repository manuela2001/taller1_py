from pydantic import BaseModel

class Administrative_staff(BaseModel):
    name:str
    code:str
    gender:str
    dependence:str
