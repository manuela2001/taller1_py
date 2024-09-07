from fastapi import APIRouter, Body
from database import GroupModel
from models.group import  Group

group_router = APIRouter()

@group_router.get("/")
def get_groups():
    groups = GroupModel.select().dicts()
    return list(groups)

@group_router.get("/{id}")
def get_group_by_id(id:int):
    try:
        group = GroupModel.get(GroupModel.id == id)
        return group
    except GroupModel.DoesNotExist:
        return {"error": "Group not found"}
    
@group_router.post("/")
def create_group(group : Group = Body(...)):
    GroupModel.create(code=group.code, semester=group.semester, student_id=group.student_id, schedule=group.schedule, subject_id=group.subject_id)
    return group

@group_router.put("/{id}")
def update_group(id:int, group: Group = Body(...)):
    updated_rows = (GroupModel.update({
        GroupModel.code : group.code,
        GroupModel.semester : group.semester,
        GroupModel.student_id : group.student_id,
        GroupModel.schedule : group.schedule,
        GroupModel.subject_id : group.subject_id
    }).where(GroupModel.id == id).execute())
    
    if updated_rows == 0:
        return {"error": "Group not found"}
    return {"message": "Group deleted successfully"}

@group_router.delete("/id")
def delete_group(id:int):
    try:
        group = GroupModel.get(GroupModel.id == id)
        group.delete_instance()
    except GroupModel.DoesNotExits:
        return{"error": "Group not found"}
    return{"message": "Group delete successfully"}