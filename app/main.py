from fastapi import FastAPI, Body
from starlette.responses import RedirectResponse
from contextlib import asynccontextmanager
from database import database as connection

from routes.student import student_router
from routes.teacher import teacher_router
from routes.subject import subject_router
from routes.group import group_router
from routes.administrative_staff import administrative_staff_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect
    try:
        yield
    finally:
        if not connection.is_close():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def read_root():
    return RedirectResponse(url='docs')

app.include_router(student_router, prefix='/students', tags=['students'])
app.include_router(teacher_router, prefix='/teachers', tags=['teachers'])
app.include_router(subject_router, prefix='/subjects', tags=['subjects'])
app.include_router(group_router, prefix='/groups', tags=['groups'])
app.include_router(administrative_staff_router, prefix='/administrative_staffs', tags=['administrative_staffs'])
