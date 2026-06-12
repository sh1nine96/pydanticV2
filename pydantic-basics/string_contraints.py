# Real companies valdates text heavily

from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=20,
    )

#Valid 
user = User(username="Shubham")    
print(user)

# Invalid

# user = User(username="Sh")
# print(user) # too short

# AI Exaample

prompt = ""

from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    prompt: str = Field(
        min_length=1,
        max_length=1000,
        description="Prompt must be between 1 and 1000 characters"
    )

# Email Validation
# Extremely common use case


from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr

# Valid

user = User(email="shubham@example.com")
print(user)

# Invalid

user = User(email="shubhamexample.com")
print(user) # Invalid email address gives ValidationError

# Industry Example - SaaS Signup

from pydantic import BaseModel, EmailStr

class CustomerSignup(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, description="Password must be at least 8 characters long")