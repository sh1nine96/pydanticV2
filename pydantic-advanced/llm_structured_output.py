# This is where AI Engineers use Pydantic daily.
# suppose Gemini returns

llm_output = {
    "customer":"Rahul",
    "sentiment":"Positive",
    "confidence":0.95
}

# create schema
from enum import Enum
from pydantic import BaseModel, Field

class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    MEUTRAL = "Neutral"

class ReviewResponse(BaseModel):
    customer: str
    sentiment: Sentiment
    confidence : float = Field(
        ge=0, le = 1
    )

#Validate

response = ReviewResponse(
    **llm_output
)
print(response)