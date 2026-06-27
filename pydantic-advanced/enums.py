# Most beginners do this

from pydantic import BaseModel
class Ticket(BaseModel):
    priority: str

# now problem with this class is that user can send
# "high", "HIGH", "urgent", "critical", "abcdxyz"

# Our solution is enum

from enum import Enum

class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

# Now we can use it

from pydantic import BaseModel

class Ticket(BaseModel):
    priority: Priority

#VAlid

Ticket(priority="High")

#Invalid
# Ticket(priority="Urgent")
#it will throw validation error

# AI Example --> Suppose a LLM classifier has possible outputs
# Positive,Negative, Neutral

from enum import Enum

class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"

class SentimentResponse(BaseModel):
    sentiment: Sentiment

# This is far more cleaner than validators


class Department(str, Enum):
    HR = "HR"
    FINANCE = "Finance"
    IT = "IT"
    OPERATIONS = "Operations"

class Employee(BaseModel):
    department: Department

emp = Employee(department="Finance")    
print(emp)    