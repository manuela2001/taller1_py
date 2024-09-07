from dotenv import load_dotenv
from peewee import *

import os


load_dotenv()


database = MySQLDatabase(
    os.getenv('MYSQL_DATABASE'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT'))
    
)
class StudentModel(Model):
    id = AutoField()
    name = CharField()
    code = CharField()
    age = IntegerField()
    semester = IntegerField()
    
    class Meta:
        database = database
        table_name = 'students'
        
class TeacherModel(Model):
    id = AutoField()
    name = CharField()
    code = CharField()
    subject_id =IntegerField()
    semester = IntegerField()
    
    class Meta:
        database = database
        table_name = 'teachers'
        
class SubjectModel(Model):
    id = AutoField()
    name = CharField()
    code = CharField()
    teacher_id = IntegerField()
    hours = IntegerField()
    semester = IntegerField()
    
    class Meta:
        database = database
        table_name = 'subjects'
        
class GroupModel(Model):
    id = AutoField()
    semester = IntegerField()
    student_id = IntegerField()
    schedule = CharField()
    subject_id = IntegerField()
    
    class Meta:
        database = database
        table_name = 'groups'
        
class Administrative_staffModel(Model):
    id = AutoField()
    name = CharField()
    code = CharField()
    gender = CharField()
    dependence = CharField()
    
    class Meta:
        database = database
        table_name = 'administrarive_staff'
        
        
    
        