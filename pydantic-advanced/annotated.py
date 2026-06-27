# We will use modern V2 style
# in V1 we often wrote

# age: int = Field(gt=18)

#but in V2 we write like this
from typing import Annotated
from pydantic import Field

age: Annotated[
    int,
    Field(gt=18)
]

# complete example

from typing import Annotated
from pydantic import BaseModel, Field

class Employee(BaseModel):

    age: Annotated[
        int,
        Field(gt = 18)
    ]

    salary: Annotated[
        float,
        Field(gt=0)
    ]

# why? bcz type and validation stay together
# This becomes extremely useful in FastAPI

# Practice --> create Product model with rules
#price>0, rating b/w 1 & 5, stock >= 0

class Product(BaseModel):
    price: Annotated[
        float,
        Field(gt=0)
    ]

    rating: Annotated[
        float,
        Field(ge=1, le=5)
    ]

    stock: Annotated[
        int,
        Field(ge=0)
    ]