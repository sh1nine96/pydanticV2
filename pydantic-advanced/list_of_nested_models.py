# Interesting --> now suppose one order contains many products

{
    'products': [
        {
            "name": "Laptop",
            "price": 50000
        },
        {
            "name": "Mouse",
            "price": 500
        }
    ]
}


# Now with pydantic 
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float


#create order model

from typing import List

class Order(BaseModel):
    products: List[Product]

order = Order(
    products = [
        {
            "name": "Laptop",
            "price": 50000
        },
        {
            "name": "Mouse",
            "price": 500
        }
    ]
)    

print(order)
print(order.products[0].name)


# AI engineering example

{
    "tasks":[
        {
            "task":"Collect Data",
            "status":"Done"
        },
        {
            "task":"Train Model",
            "status":"Pending"
        }
    ]
}

#Model

class Task(BaseModel):
    task: str
    status: str

class AgentResponse(BaseModel):
    tasks: List[Task]

#This pattern appears everywhere in CrewAI and LangGraph    