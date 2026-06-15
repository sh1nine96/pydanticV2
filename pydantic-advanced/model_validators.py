# @field_validator

# we had validated one field

#now we have @model_validator

# it validates multiple fields together

#Industry Example

# salary, experience are given

#Rule: if experience > 10, salary must be >= 100000

from pydantic import BaseModel, model_validator

class Employee(BaseModel):
    experience: int
    salary: float

    @model_validator(mode="after")
    def validate_salary(self):
        if self.experience > 10 and self.salary < 100000:
            raise ValueError(
                "Senior employees need higher salary"
            )
        return self

#valid
emp = Employee(
    experience=15,
    salary= 150000
)

print(emp)

#Invalid

# emp = Employee(
#     experience = 15,
#     salary = 50000
# )

# print(emp)

#This will raise ValueError

# AI example
#suppose confidence_score, answer
#Rule: if confidence > 0.9, answer must contain atleast 100 chars

from pydantic import BaseModel, model_validator

class AgentResponse(BaseModel):
    confidence_score: float
    answer: str

    @model_validator(mode="after")
    def check_answer_length(self):
        if self.confidence_score > 0.9 and len(self.answer) < 100:
            raise ValueError(
                "High confidence answers must be detailed (at least 100 characters)."
            )
        return self

# Valid
response = AgentResponse(
    confidence_score=0.95,
    answer="This is a very detailed response that exceeds the one hundred character limit required for high confidence scores to ensure quality and depth in the output provided by the AI agent."
)
print(response)

# Invalid
response = AgentResponse(
    confidence_score=0.98,
    answer="Too short."
)

print(response)