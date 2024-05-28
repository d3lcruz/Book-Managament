from fastapi import FastAPI
from routes import book_crud
from routes.auth import router as auth_router

app = FastAPI()
app.include_router(book_crud.router)
app.include_router(auth_router)

@app.get("/home")
async def home():
    return {"Message":"Welcome to the Book Management API"}