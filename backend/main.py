from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId
from database import products_col, cart_col

app = FastAPI()

# Allow the React frontend on port 3000 to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Convert ObjectID(_id) from MongoDB return to a plain string for JSON
def to_dict(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


@app.get("/products")
def get_products():
    return [to_dict(p) for p in products_col.find()]


# Structure for Requesting cart item
class CartItemRequest(BaseModel):
    product_id: str
    name: str
    price: float
    image: str


@app.get("/cart")
def get_cart():
    return [to_dict(i) for i in cart_col.find()]


@app.post("/cart")
def add_to_cart(item: CartItemRequest):
    existing = cart_col.find_one({"product_id": item.product_id})

    # if the requested product is already in cart, just increase the quantity
    if existing:
        cart_col.update_one({"product_id": item.product_id}, {"$inc": {"quantity": 1}})
        return to_dict(cart_col.find_one({"product_id": item.product_id}))
    new_item = {
        "product_id": item.product_id,
        "name": item.name,
        "price": item.price,
        "image": item.image,
        "quantity": 1,
    }
    result = cart_col.insert_one(new_item)
    new_item["id"] = str(result.inserted_id)
    del new_item["_id"]
    return new_item


class QuantityRequest(BaseModel):
    quantity: int


@app.put("/cart/{item_id}")
def update_quantity(item_id: str, body: QuantityRequest):

    # if the request has quantity less than 1, raise HTTPException
    if body.quantity < 1:
        raise HTTPException(status_code=400, detail="Quantity must be at least 1")
    
    result = cart_col.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"quantity": body.quantity}}
    )

    # if the requested product is not in the cart, raise HTTPException
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return to_dict(cart_col.find_one({"_id": ObjectId(item_id)}))


@app.delete("/cart/{item_id}")
def remove_from_cart(item_id: str):
    result = cart_col.delete_one({"_id": ObjectId(item_id)})

    # if the requested product is not in the cart, raise HTTPException
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return {"message": "Item removed"}
