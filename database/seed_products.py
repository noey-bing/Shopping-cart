"""
Need to run this script to load your products into MongoDB whenever there's any changes to products list.

HOW TO USE:
  1. Edit the `products` list below and add your own items.
  2. Run this script from the terminal:
       python3 database/seed_products.py
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from backend.database import products_col

products = [
    {
        "name": "Wireless Headphones",
        "price": 80.00,
        "description": "Sony Beige Headphones",
        "image": "https://m.media-amazon.com/images/I/41fn3hNjnRL._AC_SL1000_.jpg"
    },

    {
        "name": "Lamp",
        "price": 23.00,
        "description": "Green Cordless LED Lamp",
        "image": "https://img.zcdn.com.au/lf/50/hash/38080/20539220/4/22cm+Eton+LED+Portable+Lamp.jpg"
    },

    {
        "name": "Cargo Pants",
        "price": 55.00,
        "description": "Dark Green Cargo Pants",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqA6gQe7slBTrryPOJp3e9F84Ujn4hL6O_4Q&s"
    },


    {
        "name": "Guitar",
        "price": 120.00,
        "description": "Basic Guitar for Beginner",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToDGP9QQAeDs83c8iu2D5UPAUJzVNR7UbHvQ&s"
    },

    {
        "name": "Digital Camera",
        "price": 150.00,
        "description": "Y2K Vintage Digital Camera",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQk6epEegbaXLNswDEauZCqEMfA3vhcIC9QOg&s"
    },

    {
        "name": "DIY Miniature",
        "price": 93.00,
        "description": "Forest Adventure DIY Miniature Kit",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqVYhHCVwfKbX57P37e6I5qMoBFxeBZqifMw&s"
    },

    {
        "name": "Shoulder Bag",
        "price": 230.00,
        "description": "Mini Black Shoulder Bag",
        "image": "https://s7d2.scene7.com/is/image/Coach/cdb19_svbk_a0?$desktopProduct$"
    },

    {
        "name": "MP3 Player",
        "price": 110.00,
        "description": "Vintage MP3 Player",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRviKT9YecU-5wCIRsFDlG3UyA0OWvH3hIkfg&s"
    }

]

# Clear existing products then insert the updated list (to avoid duplicates)
products_col.delete_many({})

if not products:
    print("⚠️  No products found. Please add products to the list above.")
else:
    products_col.insert_many(products)
    print(f"✅  Inserted {len(products)} products into the database.")
