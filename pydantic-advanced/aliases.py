# Very common when integrating APIs.
# Suppose external API sends:

{
    "userName":"Shubham",
    "userAge":25
}

# but company standard is:
# name
# age

#here we use aliases

from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(alias='username')
    age: int = Field(alias='userAge')

user = User(
    username="Arun",
    userAge=35
)

print(user.name)
print(user.age)

# AI example --> Gemini:
# confidenceScore or confidence_score can be used as alias
