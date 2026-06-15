# sometimes keys are unknown

#Example

{
    "sales": {
        "Jan":1000,
        "Feb":1500,
        "Mar":3000
    }
}

# months change dynamically

# Use Dict

from typing import Dict
from pydantic import BaseModel

class SalesReport(BaseModel):
    sales: Dict[str, int]

report = SalesReport(
    sales = {
        "Jan": 1000,
        "Feb": 2000,
        "Mar": 3000
    }
)    

print(report)
print(report.sales["Jan"])


# AI engineering example

{
    "token_usage":{
        "prompt_tokens": 500,
        "completion_tokens": 100,
        "total_tokens": 600
        }    
}

#Use dict
