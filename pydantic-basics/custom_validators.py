# Suppose there is a company policy :
# name can't contain numbers

#Pydantic doesn't have built in validator for this but we can easily create custom validators

#Pydantic V2 syntax for custom validators

from pydantic import BaseModel
from pydantic import field_validator

class Employee(BaseModel):
    name: str
    
    @field_validator('name')
    @classmethod
    def validate_name(cls, value):

        if any(char.isdigit() for char in value):
            raise ValueError(
                "Name cannot contain numbers"
            )
        return value

#Valid    
emp = Employee(name="Shubham")
print(emp) 

#Invalid
# emp = Employee(name="Shubham123")
# print(emp) # raises ValidationError: Name cannot contain numbers

# AI Industry Example
#Suppose LLM sentiment output should only be:

#Positive, Negative, Neutral
#Nothing else is allowed

from pydantic import BaseModel
from pydantic import field_validator

class SentimentResponse(BaseModel):
    sentiment: str

    @field_validator("sentiment")
    @classmethod
    def validate_sentiment(cls, value):

        allowed = [
            "Positive",
            "Negative",
            "Neutral"
        ]

        if value not in allowed:
            raise ValueError(
                f"Sentiment must be one of {allowed}"
            )
        return value
    
#Valid 

sentiment = SentimentResponse(sentiment="Positive")
print(sentiment) 

#Invalid

# sentiment = SentimentResponse(sentiment="Happy")
# print(sentiment) 
# raises ValidationError: 
# Sentiment must be one of ['Positive', 'Negative', 'Neutral']

#Real AI Engineer Example

#Imagine Gemini returns

{
    "customer_name": "Shubham",
    "sentiment": "Amazing",
    "score": 1.5
}

# Bad Output

#Production Validation

from pydantic import BaseModel, Field, field_validator

class ReviewAnalysis(BaseModel):

    customer_name: str
    sentiment: str
    score: float = Field(ge=0, le=1)

    @field_validator("sentiment")
    @classmethod
    def validate_sentiment(cls, value):

        allowed = [
            "Positive",
            "Negative",
            "Neutral"
        ]

        if value not in allowed:
            raise ValueError(
                f"Sentiment must be one of {allowed}"
            )
        return value
    
# Valid
# 
review = ReviewAnalysis(
    customer_name="Shubham",
    sentiment="Positive",
    score=0.8
)
print(review)  


# Invalid

review = ReviewAnalysis(
    customer_name="Shubham",
    sentiment="Happy",
    score=0.8
)