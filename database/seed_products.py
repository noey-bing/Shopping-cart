"""
Need to run this script to load your products into MongoDB.

HOW TO USE:
  1. Edit the `products` list below and add your own items.
  2. Run this script once from the terminal:
       python database/seed_products.py

EACH PRODUCT NEEDS FOUR FIELDS:
  - name        : product name (string)
  - price       : price in dollars, e.g. 19.99 (number)
  - description : a short description shown on the card (string)
  - image       : a URL to a product image (string)
                  → Free placeholder images: https://picsum.photos/300/200
                  → Or use any image URL you find online

EXAMPLE PRODUCT:
  {
      "name": "Wireless Headphones",
      "price": 49.99,
      "description": "Bluetooth headphones with noise cancellation.",
      "image": "https://picsum.photos/seed/headphones/300/200"
  }
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from backend.database import products_col

# ─────────────────────────────────────────────────
# TODO: Add your products here.
# Copy the example block and fill in your own values.
# You can add as many products as you want.
# ─────────────────────────────────────────────────
products = [
    {
        "name": "Headphones",
        "price": 80.00,
        "description": "Sony Beige Headphones",
        "image": "https://m.media-amazon.com/images/I/41fn3hNjnRL._AC_SL1000_.jpg"
    },

    # ── Product 2 ──────────────────────────────────
    # {
    #     "name": "YOUR PRODUCT NAME",
    #     "price": 0.00,
    #     "description": "YOUR DESCRIPTION",
    #     "image": "YOUR IMAGE URL"
    # },

    # ── Product 3 ──────────────────────────────────
    # {
    #     "name": "YOUR PRODUCT NAME",
    #     "price": 0.00,
    #     "description": "YOUR DESCRIPTION",
    #     "image": "YOUR IMAGE URL"
    # },

]
# ─────────────────────────────────────────────────


# Clear existing products and insert the new list
products_col.delete_many({})

if not products:
    print("⚠️  No products found. Please add products to the list above.")
else:
    products_col.insert_many(products)
    print(f"✅  Inserted {len(products)} products into the database.")
