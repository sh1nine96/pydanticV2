from pydantic import BaseModel, Field

class Product(BaseModel):
    product_name: str
    price: float = Field(gt=0, description="Price must be greater than 0")
    stock: int = Field(ge=0, description="Stock must be greater than or equal to 0")
    rating: float = Field(ge=1, le=5, description="Rating must be between 1 and 5")

# Invalid Data Test

product = Product(
    product_name = "iphone 14",
    price = -70000,
    stock = -5,
    rating = 6
)

# We get validation errors for price, stock, and rating because:
# - Price must be greater than 0, but we passed -70000
# - Stock must be greater than or equal to 0, but we passed -5
#  Rating must be between 1 and 5, but we passed 6


