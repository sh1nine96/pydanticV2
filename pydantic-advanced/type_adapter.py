# it is one of the most underrated Pydantic V2 features

# suppose you don't want a model
# you only want validation

# without model
['python', 'SQL', 'Pandas']

#Need Validation
from pydantic import TypeAdapter
adapter = TypeAdapter(
    list[str]
)

skills = adapter.validate_python(
    ['Python', 'SQL', 'Power BI']
)

print(skills) # it will work

# adapter.validate_python(
#     123
# )  This will be the error

# AI example
#LLM returns
['Machine Learning', 'Python', 'SQL']

response = adapter.validate_python(
    ['Machine Learning', 'Python', 'SQL']
)

print(response)