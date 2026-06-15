# This is very close to what you'll use with Gemini/OpenAI

from typing import List
from pydantic import BaseModel, Field

class ToolCall(BaseModel):
    tool_name: str
    status: str

class AgentResponse(BaseModel):
    query: str
    final_answer: str
    confidence: float = Field(
        ge=0,
        le= 1
    )
    tools_used: List[ToolCall]

response = AgentResponse(
    query = "Top Python Libraries",
    final_answer = "Pandas, Numpy....",
    confidence = 0.92,
    tools_used = [
        {
            "tool_name": "Google Search",
            "status": "Success"
        },
        {
            "tool_name": "Vector DB",
            "status": "Success"
        }
    ]
) 

#Access

print(response.query)
print(response.final_answer)
print(response.tools_used[0].tool_name)