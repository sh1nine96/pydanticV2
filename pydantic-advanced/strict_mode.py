

# BY default age = '25'  becomes 25
#pydantic converts it automatically
# but its dangerous sometimes
#example: Financial systems, Healthcare systems, Banking systems

#Use strict Types:

from pydantic import BaseModel, StrictInt, StrictFloat

class Employee(BaseModel):
    age: StrictInt

# Valid 
age = 25

#Invalid
# emp = Employee (
#     age = '25'
# )

class BankAccount(BaseModel):
    account_number: StrictInt
    balance: StrictFloat

#Invalid
myaccount = BankAccount(
    account_number= 123456789,
    balance= '42527282'
)