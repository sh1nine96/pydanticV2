#CHALLENGE 1 --> Recruitment Platform
# Create a class Candidate with the following attributes:
# name: str, email, experience, expected_salary
# Rules: experience >= 0, expeted_salary > 0, email valid, 
# name should not contain numbers


#CHALLENGE 2 --> LLM Output Validation
# Create class TicketClassifier with attributes:
# ticket_text, priority, department
# Rules:  Priority(low, medium, high, critical), 
# Department(IT, HR, Finance, Operations)
#Use custom validators

#CHALLENGE 3 --> RAG system

# create class AnswerResponse with attributes:
# answer, confidence_score, source_document
#Rules: confidence_score between 0 and 1, answer minimum 20 chars, source_document minimum 5 chars

## Bonus --> Build this exactly 

from pydantic import BaseModel,  field_validator

class LLMResponse(BaseModel):
    query: str
    answer: str
    confidence: float
    model_name: str

# Validation --> query min length 5, answer min length 20, confidence between 0 and 1
#  model_name only: gemini, gpt or claude using @field_validator
