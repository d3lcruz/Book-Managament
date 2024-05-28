from fastapi import APIRouter, HTTPException
from pymongo import ReturnDocument
from database.client import collection
from bson import ObjectId
from models.books_model import Book
from database.schemas.schemas_confi import list_serial, individual_serial 

router = APIRouter(prefix="/book",
                   tags=["book"],
                   responses={404:{"message":"No found"}})

# Add books
@router.get("/", response_model=list[Book])
async def get_todo():
    book = list_serial(collection.find())
    return book


@router.post("/", response_model= Book)
async def add_book(book:Book):
    book_dict = book.dict(exclude_unset=True)
    
    try:
        new_book = collection.insert_one(book_dict)
        book.book_id = str(new_book.inserted_id)
    except:
        raise HTTPException(status_code=500, detail="Error inserting book into the database")
    
    return book_dict

@router.get("/{book_id}", response_model= Book)
async def read_book(book_id:str):
    try:
        objc_id = ObjectId(book_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error id")
    
    read_book = collection.find_one({"_id": objc_id})
    if read_book is None:
        raise HTTPException(status_code=500, detail="Error inserting book id")
    
    read_book["book_id"] = str(read_book["_id"])
    return Book(**read_book)

@router.put("/{book_id}", response_model= Book)
async def update_book(book_id:str, book: Book):
    book_dict = book.dict(exclude_unset=True)
    try:
        objc_id = ObjectId(book_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error id")
    
    update_book = collection.find_one_and_update({"_id": objc_id}, {"$set": book_dict}, return_document=ReturnDocument.AFTER)
    
    if update_book is None:
        raise HTTPException(status_code=500, detail="Error inserting book id")
    
    update_book["book_id"] = str(update_book["_id"])
    return Book(**update_book)

@router.delete("/{book_id}", response_model=Book)
async def clean_book(book_id:str):
    try:
        objc_id = ObjectId(book_id)
    except:
        raise HTTPException(status_code=500, detail="Error id")
    
    clean = collection.find_one_and_delete({"_id": objc_id})
    if clean is None:
        raise HTTPException(status_code=500, detail="Error inserting book id")

    clean["book_id"] = str(clean["_id"])
    del clean["_id"]
    return Book(**clean)
    