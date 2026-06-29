# Real APIs return JSON

from pydantic import BaseModel
#creating model
class Employee(BaseModel):
    name: str
    age: int

emp = Employee(
    name='Shubham',
    age = 25
)

# dictionary
print(emp.model_dump())

#JSON
print(emp.model_dump_json())
#this will return JSON, 
# very common in FastAPI, LangChain, MCP, Gemini. OpenAI etc