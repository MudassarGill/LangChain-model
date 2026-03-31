from pydantic import BaseModel


class Student(BaseModel):
    name:str 
    

new_student={'name':'Mudassar'}

student=Student(**new_student)
print(student)