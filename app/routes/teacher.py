from fastapi import APIRouter, Body
from database import TeacherModel
from models.teacher import  Teacher

teacher_router = APIRouter()

@teacher_router.get("/")
def get_teachers():
    teachers = TeacherModel.select().dicts()
    return list(teachers)

@teacher_router.get("/{id}")
def get_teacher_by_id(id:int):
    try:
        teacher = TeacherModel.get(TeacherModel.id == id)
        return teacher
    except TeacherModel.DoesNotExist:
        return {"error": "Teacher not found"}
    
@teacher_router.post("/")
def create_teacher(teacher : Teacher = Body(...)):
    TeacherModel.create(name=teacher.name, code=teacher.code, subject_id=teacher.subject_id, semester=teacher.semester)
    return teacher

@teacher_router.put("/{id}")
def update_teacher(id:int, teacher: Teacher = Body(...)):
    updated_rows = (TeacherModel.update({
        TeacherModel.name : teacher.name,
        TeacherModel.code : teacher.code,
        TeacherModel.subject : teacher.subject,
        TeacherModel.semester : teacher.semester
    }).where(TeacherModel.id == id).execute())
    
    if updated_rows == 0:
        return {"error": "Teacher not found"}
    return {"message": " Teacher update successfully"}

@teacher_router.delete("/id")
def delete_tecaher(id:int):
    try:
        teacher = TeacherModel.get(TeacherModel.id == id)
        teacher.delete_instance()
    except TeacherModel.DoesNotExits:
        return{"error": "Teacher not found"}
    return{"message": "Teacher delete successfully"}