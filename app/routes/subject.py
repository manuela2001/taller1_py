from fastapi import APIRouter, Body
from database import SubjectModel
from models.subjetc import  Subject

subject_router = APIRouter()

@subject_router.get("/")
def get_subjects():
    subjects = SubjectModel.select().dicts()
    return list(subjects)

@subject_router.get("/{id}")
def get_subject_by_id(id:int):
    try:
        subject = SubjectModel.get(SubjectModel.id == id)
        return subject
    except SubjectModel.DoesNotExist:
        return {"error": "Subject not found"}
    
@subject_router.post("/")
def create_subject(subject : Subject = Body(...)):
    SubjectModel.create(name=subject.name, code=subject.code, teacher_id=subject.teacher_id, hours=subject.hours, semester=subject.semester)
    return subject

@subject_router.put("/{id}")
def update_subject(id:int, subject : Subject = Body(...)):
    updated_rows = (SubjectModel.update({
        SubjectModel.name : subject.name,
        SubjectModel.code : subject.code,
        SubjectModel.teacher_id : subject.teacher_id,
        SubjectModel.hours : subject.hours,
        SubjectModel.semester : subject.semester
    }).where(SubjectModel.id == id).execute())
    
    if updated_rows == 0:
        return {"error": "Subject not found"}
    return {"message": "Subject update successfully"}

@subject_router.delete("/id")
def delete_subject(id:int):
    try:
        subject = SubjectModel.get(SubjectModel.id == id)
        subject.delete_instance()
    except SubjectModel.DoesNotExits:
        return{"error": "subject not found"}
    return{"message": "subject delete successfully"}