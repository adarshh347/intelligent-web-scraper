from pydantic import BaseModel
# BaseModel like a "smart template" for your data —
#  it enforces types and auto-generates schemas.

class Venue(BaseModel):
    name: str
    location: str
    price: str
    capacity: str
    rating: float
    reviews: int
    description: str
# This ensures that whenever you create a Venue, 
# the fields must match the types you declared.

