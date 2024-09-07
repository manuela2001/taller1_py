from fastapi import APIRouter, Body
from database import StudentModel
from models.student import  Student

student_router = APIRouter()

@student_router.get("/")
def get_students():
    students = StudentModel.select().dicts()
    return list(students)

@student_router.get("/{id}")
def get_student_by_id(id:int):
    try:
        student = StudentModel.get(StudentModel.id == id)
        return student
    except StudentModel.DoesNotExist:
        return {"error": "Student not found"}
    
@student_router.post("/")
def create_student(student : Student = Body(...)):
    StudentModel.create(name=student.name, code=student.code, age=student.age, semester=student.semester)
    return student

@student_router.put("/{id}")
def update_student(id:int, student: Student = Body(...)):
    updated_rows = (StudentModel.update({
        StudentModel.name : student.name,
        StudentModel.code : student.code,
        StudentModel.age : student.age,
        StudentModel.semester : student.semester
    }).where(StudentModel.id == id).execute())
    
    if updated_rows == 0:
        return {"error": "student not found"}
    return {"message": "Student update successfully"}
        
@student_router.delete("/id")
def delete_student(id:int):
    try:
        student = StudentModel.get(StudentModel.id == id)
        student.delete_instance()
    except StudentModel.DoesNotExits:
        return{"error": "student not found"}
    return{"message": "student delete successfully"}
    
