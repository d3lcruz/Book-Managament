from typing import Optional, List
from pydantic import BaseModel

class Book(BaseModel):
    book_id: Optional[str] = None
    title: str
    description: str
    author: str