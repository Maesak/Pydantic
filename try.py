from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    email: EmailStr
    address: Address

@app.post("/register")
def register_user(user: User): 
    return {
        "message": f"Welcome {user.name}!",
        "user_data": user.model_dump()
    }
