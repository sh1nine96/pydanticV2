# Real systems often derive values

price = 1000
quantity = 5

# we need 
total = 5000

# we dont store total, we calculate it

from pydantic import BaseModel, computed_field

class Order(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total(self)->float:
        return self.price * self.quantity
    
order = Order(
    price=2000,
    quantity=8
)

print(order.total) #16000.0

# Even
print(order.model_dump())

#will print {'price': 2000.0, 'quantity': 8, 'total': 16000.0}

#AI Example

tokens = 1000
cost_per_token = 0.02

# calculate total_cost

class Token_economy(BaseModel):
    tokens: int
    cost_per_token: float

    @computed_field
    @property
    def total_cost(self)->float:
        return self.tokens * self.cost_per_token
    
cost = Token_economy(
    tokens=1000000,
    cost_per_token=0.015
)

print(cost.total_cost)

print(cost.model_dump())