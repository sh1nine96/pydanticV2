# Suppose you're building an HR onboarding system for a company.

#Without Validation

employee = {
    "name": "John Faulkner",
    "age": -25,
    "salary": -50000
}

# Here database accepts garbage data without any validation, 
# which can lead to issues down the line when we try to use this data for payroll, benefits, etc.
# Business gets corrupted

#Solution with Pydantic: Field Constraints

from pydantic import BaseModel, Field

class Employee(BaseModel):
    name: str
    age: int = Field(gt = 18, description="Age must be greater than or equal to 18")
    salary: float = Field(gt = 0, description="Salary must be greater than 0")


#Test 1: Valid Data

emp = Employee(
    name="John Faulkner",
    age=30,
    salary=50000
)

print(emp)

# it works fine and we get the expected output


#Test 2: Invalid Data

emp = Employee(
    name = "John Faulkner",
    age = 10,
    salary = 50000
)

# We get a validation error because age is less than 18, 
# which is not allowed according to our model constraints.
# bcz age must be greater than or equal to 18 for an employee in our system.

# Common Constraints:
# gt: Greater than
# Field(gt=0) means the value must be greater than 0
# ge: Greater than or equal to
# Field(ge=18) means the value must be greater than or equal to 18
# lt: Less than
# Field(lt=100) means the value must be less than 100
# le: Less than or equal to
# Field(le=65) means the value must be less than or equal to 65
