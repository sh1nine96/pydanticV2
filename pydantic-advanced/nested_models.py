# Now we will enter the part of pydantic that is heavily used in FasAPI, AI agents,
# Langraph, CrewAI, MCP Servers, RAG systems & enterprise APIs

#Lets say gemini returns

{
    "customer": {
        "name": "Rahul",
        "email": "rahul@gmail.com"
    },
    "order_amount": 5000
}

#this is not a flat structure

# Real APIs almost never returns
{
    "name": "Rahul",
    "email": "rahul@gmail.com"
}

#Instead
{
    "customer": {...},
    "orders": [...],
    "payment": {...}
}

#This is where nested module comes in

## Nested Modules

#without pydantic

data = {
    "customer": {
        "name": "Rahul",
        "email": "rahul@gmail.com"
    }
}

print(data["customer"]["name"])

# with pydantic

from pydantic import BaseModel, EmailStr

class Customer(BaseModel):
    name: str
    email: EmailStr

#Now create another model


class Order(BaseModel):
    customer: Customer
    amount: float

#Input

order = Order(
    customer={
        "name": "Rahul",
        "email": "rahul@gmail.com"
    },
    amount= 5000.0
)

# access
print(order.customer.name)
print(order.customer.email)
print(order.amount)

#Industry example --> Amazon Order API
{
    "customer": {
        "name": "Rahul",
        "email": "rahul@gmail.com"
    },
    "amount": 5000.0,
}

#customer is its own object, Order is another object

#Practice build Class Address with fields city, state and country
#Then employee with fields name, salary and address

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    country: str

class Employee(BaseModel):
    name: str
    salary: float
    address: Address

emp = Employee(
    name = "Ajay",
    salary = 50000.0,
    address = {
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India"
    }
)

print(emp)
print(emp.address.city)
print(emp.address.state)
print(emp.address.country)