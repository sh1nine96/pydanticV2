# Lets first understand why Pydantic is needed. We will start with a simple example

user = {
    "name": "Jumairah",
    "age": "30",
    "salary": "50000.0"
}

print(user["name"])  # This will work fine
#print(user["age"] + 5)  # This will raise an error because age is a string, not an integer

#why it happens bcz
print(type(user["age"]))  # This will show that age is a string

# but we want age to be an integer and salary to be a float. 

#Without pydantic, we would have to manually convert these values every time we use them, which can be error-prone and tedious.

age = int(user["age"])
salary = float(user["salary"])
#Imagine doing this for 1000 fields in a large application. 
# It would be a nightmare to maintain and debug.

# This is where Pydantic comes in. 
# It allows us to define a model with the expected types for each field, 
# and it will automatically validate and convert the input data to the correct types.

from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    salary: float

emp = Employee(
    name = "Shubham",
    age = "30",
    salary = "50000.0"
)  

print(emp)
print(emp.name)  # This will work fine
print(type(emp.age))   # This will work fine and will be an integer
print(type(emp.salary)) # This will work fine and will be a float


# Example

class Student(BaseModel):
    name: str
    course: str
    fees: float

student = Student(
    name = "Alice",
    course = "Computer Science",
    fees = "15000.0"
)    

print(student)
print(student.name)  # This will work fine
print(type(student.fees))


# Example 2 with Validation error

class Employee(BaseModel):
    name: str
    age: int
    salary: float


# emp = Employee(
#     name = "Shubham",
#     age = "thirty",  # This will raise a validation error because it cannot be converted to an integer
#     salary = "50000.0"
# )    

# print(emp)


#Example 3 with Optional fields
from typing import Optional
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    phone: Optional[str] = None

emp = Employee(
    name = "Shubham",
    age = 30
)    

print(emp)


# Example 4 with default values

from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int
    country: str = "India"


emp = Employee(
    name = "Shubham",
    age = 30
)

print(emp)

# Example 5 with Export Model

class Employee(BaseModel):
    name: str
    age: int

emp = Employee(
    name = "Shubham",
    age = 30
)

print(emp.model_dump())  # This will return a dictionary representation of the model


# Example 6 with JSON Conversion

# This is very common in AI Engineering when we want to send data to an API or save it in a file.
print(emp.model_dump_json())  # This will return a JSON string representation of the model

# LLMs, APIs, FAST API, Langchain etc. often require data in JSON format, 
# so this feature is very useful for AI Engineers.

#Real AI Engineer use case:
#suppose Gemini returns
response = {
    "name": "Rahul",
    "sentiment": "positive",
    "score": 0.95
}

# now we validate it using pydantic

from pydantic import BaseModel

class SentimentResponse(BaseModel):
    name: str
    sentiment: str
    score: float

validated_response = SentimentResponse(**response)    

print(validated_response)
