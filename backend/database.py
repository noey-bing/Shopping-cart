import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# Connect to MongoDB
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)
db = client["shopdb"]

# Two databases in total: one for products, one for the cart
products_col = db["products"]
cart_col = db["cart"]
