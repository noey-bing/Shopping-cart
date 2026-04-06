from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId
from database import products_col, cart_col

app = FastAPI()

# Allow the React frontend (running on port 3000) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper: convert MongoDB document to a plain dict (MongoDB uses _id, we convert to id)
def to_dict(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


# ─── PRODUCTS ─────────────────────────────────────────────────────────────────

# READ: Get all products
@app.get("/products")
def get_products():
    products = list(products_col.find())
    return [to_dict(p) for p in products]


# ─── CART ─────────────────────────────────────────────────────────────────────

# Request body shape for adding an item to the cart
class CartItemRequest(BaseModel):
    product_id: str
    name: str
    price: float
    image: str


# READ: Get all items currently in the cart
@app.get("/cart")
def get_cart():
    items = list(cart_col.find())
    return [to_dict(i) for i in items]


# CREATE: Add a product to the cart
# If the product is already in the cart, increase its quantity by 1
@app.post("/cart")
def add_to_cart(item: CartItemRequest):
    existing = cart_col.find_one({"product_id": item.product_id})

    if existing:
        # Product already in cart → increase quantity
        cart_col.update_one(
            {"product_id": item.product_id},
            {"$inc": {"quantity": 1}}
        )
        updated = cart_col.find_one({"product_id": item.product_id})
        return to_dict(updated)
    else:
        # New item → insert with quantity 1
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


# UPDATE: Change the quantity of a cart item
class QuantityRequest(BaseModel):
    quantity: int

@app.put("/cart/{item_id}")
def update_quantity(item_id: str, body: QuantityRequest):
    if body.quantity < 1:
        raise HTTPException(status_code=400, detail="Quantity must be at least 1")

    result = cart_col.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"quantity": body.quantity}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Cart item not found")

    updated = cart_col.find_one({"_id": ObjectId(item_id)})
    return to_dict(updated)


# DELETE: Remove an item from the cart
@app.delete("/cart/{item_id}")
def remove_from_cart(item_id: str):
    result = cart_col.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cart item not found")
    return {"message": "Item removed"}
