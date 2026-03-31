from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name:str 
    age:Optional[int]=None
    

new_student={'name':'Mudassar'}

student=Student(**new_student)
print(student)