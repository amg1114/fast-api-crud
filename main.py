from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

class Item(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float
    quantity: int
    image_url: str
    
description = """
## FastAPI CRUD Example
This is a simple CRUD API using FastAPI. You can create, read, update, and delete items.
### Create Item
- **Endpoint:** `/items/`
- **Method:** `POST`
- **Request Body:** JSON object with item details.
### Read Item
- **Endpoint:** `/items/{item_id}`
- **Method:** `GET`
- **Path Parameter:** `item_id` (integer)
- **Response:** JSON object with item details.
### Update Item
- **Endpoint:** `/items/{item_id}`
- **Method:** `PUT`
- **Path Parameter:** `item_id` (integer)
- **Request Body:** JSON object with updated item details.
### Delete Item
- **Endpoint:** `/items/{item_id}`
- **Method:** `DELETE`
- **Path Parameter:** `item_id` (integer)
- **Response:** JSON object with a success message.
"""

data: list[Item] = []
app = FastAPI(
    title="FastAPI CRUD Example",
    description=description,
    summary_description="This API allows you to manage items.",
    version="1.0.0",
    contact={
        "name": "Johan Alejandro Moreno",
        "url": "https://github.com/amg1114"
    }
)

@app.post("/items/")
def create_item(item: Item):
    data.append(item)
    return item  

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = next((cItem for cItem in data if cItem.id == item_id), None)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    for cItem in data:
        if cItem.id == item_id:
            cItem.id = item.id
            cItem.name = item.name
            return cItem
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global data
    data = [item for item in data if item.id != item_id]
    
    if not any(item.id == item_id for item in data):
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"message": "Item deleted successfully"}
