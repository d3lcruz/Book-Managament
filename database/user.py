from passlib.context import CryptContext
from .client import users_collection

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(username: str):
    return users_collection.find_one({"username": username})

def create_user(user):
    user["hashed_password"] = pwd_context.hash(user["password"])
    del user["password"]
    users_collection.insert_one(user)
    return user
