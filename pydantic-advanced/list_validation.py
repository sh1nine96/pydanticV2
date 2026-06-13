# Real APIs return lists everywhere
#Example

{
    "skills": [
        "Python",
        "SQL",
        "Pandas"
    ]
}

#Pydantic

from typing import List
from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    skills: List[str]

#Input

candidate = Candidate(
    name = "Shubham",
    skills = [
        "Python",
        "SQL",
        "Pandas",
        "Machine Learning",
        "Deep Learning"
    ]
)    

print(candidate)
print(candidate.skills)

#Validation Happens Automatically

#Wrong

# candidate = Candidate(
#     name = "Rahul",
#     skills = 123
# )
#This will be an error bcz skills must be a List

#Industry Example --> Resume Parser

{
    "name": "Shubham",
    "skills": [
        "Python",
        "SQL",
        "Pandas",
        "Machine Learning",
        "Deep Learning"
    ]
}

# This is exactly how parsed resumes are stored

#Practice -> Create class Student, Field: name, subjects (List[str])

class Student(BaseModel):
    name: str
    subjects: List[str]

student = Student(
    name = "Shubham",
    subjects = [
        "Python",
        "SQL",
        "Pandas",
        "Machine Learning",
        "Deep Learning"
    ]
)    

print(student)
