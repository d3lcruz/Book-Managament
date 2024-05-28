def individual_serial(book) -> dict:
    return {
        "id": str (book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "description": book["description"]
    }
    
def list_serial(books) -> list:
    return[individual_serial(book) for book in books]

def user_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user.get("full_name"),
        "disabled": user.get("disabled")
    }

def users_serial(users) -> list:
    return [user_serial(user) for user in users]
