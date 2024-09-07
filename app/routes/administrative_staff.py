from fastapi import APIRouter, Body
from database import Administrative_staffModel
from models.administrative_staff import  Administrative_staff

administrative_staff_router = APIRouter()

@administrative_staff_router.get("/")
def get_administrative_staffs():
    administrative_staffs = Administrative_staffModel.select().dicts()
    return list(administrative_staffs)

@administrative_staff_router.get("/{id}")
def get_administrative_staff_by_id(id:int):
    try:
        administrative_staff = Administrative_staffModel.get(Administrative_staff.id == id)
        return administrative_staff
    except Administrative_staffModel.DoesNotExist:
        return {"error": "Administrative_staff not found"}
    
@administrative_staff_router.post("/")
def create_administrative(administrative_staff : Administrative_staff = Body(...)):
    Administrative_staffModel.create(name=administrative_staff.name, code=administrative_staff.code, gender=administrative_staff.gender, dependence=administrative_staff.semester)
    return administrative_staff

@administrative_staff_router.put("/{id}")
def update_teacher(id:int, administrative_staff: Administrative_staff = Body(...)):
    updated_rows = (Administrative_staffModel.update({
        Administrative_staffModel.name : administrative_staff.name,
        Administrative_staffModel.code : administrative_staff.code,
        Administrative_staffModel.gender : administrative_staff.gender,
        Administrative_staffModel.dependence : administrative_staff.dependence
    }).where(Administrative_staffModel.id == id).execute())
    
    if updated_rows == 0:
        return {"error": "Administrative staff not found"}
    return {"message": " Administrative staff update successfully"}

@administrative_staff_router.delete("/id")
def delete_admnistrative_staff(id:int):
    try:
        administrative_staff = Administrative_staffModel.get(Administrative_staffModel.id == id)
        administrative_staff.delete_instance()
    except Administrative_staffModel.DoesNotExits:
        return{"error": "Administrative staff not found"}
    return{"message": "Administrative staff delete successfully"}