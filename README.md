# ShopCart — E-Commerce Shopping Cart

A single-page web application that lets users browse products, add items to a cart, adjust quantities, and remove items. Built as an individual assignment demonstrating HTML, CSS, JavaScript, React, Python, FastAPI, and MongoDB.

---

## Problem Statement

Users need a simple way to browse products and manage a shopping cart — adding items, changing how many they want, and removing ones they no longer need — all without page reloads.

---

## Technical Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Frontend   | React 18 (Vite)                   |
| Styling    | CSS (single stylesheet)           |
| Routing    | React state (SPA, no router lib)  |
| Backend    | Python + FastAPI                  |
| Database   | MongoDB with pymongo              |
| Deployment | Local (see setup below)           |

---

## Features

- View all products displayed in a responsive grid
- Add a product to the cart (quantity increases if already added)
- Change the quantity of any cart item using +/− buttons
- Remove an item from the cart with one click
- Live cart item count badge in the header
- Cart total price calculated automatically
- Single-page — no full page reloads

---

## Folder Structure

```
/
├── frontend/              React frontend (Vite)
│   ├── src/
│   │   ├── App.jsx        Root — manages all state and API calls
│   │   ├── ProductList.jsx  Product grid view
│   │   ├── Cart.jsx         Cart view
│   │   └── index.css      All styles
│   └── index.html         Single HTML file (SPA entry point)
│
├── backend/               FastAPI backend
│   ├── main.py            All API routes (products + cart CRUD)
│   ├── database.py        MongoDB connection
│   └── requirements.txt
│
├── database/
│   └── seed_products.py   ← Add your products here, then run this script
│
└── README.md
```

---

## Getting Started

### 1. Start MongoDB
```bash
brew services start mongodb-community
```

### 2. Install and run the backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --port 8000
```

### 3. Add products to the database
Open `database/seed_products.py`, fill in your products, then run:
```bash
python database/seed_products.py
```

### 4. Install and run the frontend
```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

---

## API Endpoints

| Method | Endpoint         | Description                        |
|--------|------------------|------------------------------------|
| GET    | `/products`      | Get all products                   |
| GET    | `/cart`          | Get all cart items                 |
| POST   | `/cart`          | Add a product to the cart          |
| PUT    | `/cart/{id}`     | Update cart item quantity          |
| DELETE | `/cart/{id}`     | Remove an item from the cart       |

---

## Challenges Overcome

Keeping the cart state in sync with the database required re-fetching cart data after every mutation (add, update, delete), which ensured the UI always reflected the true database state rather than an out-of-sync local copy. Handling the "add to cart" logic on the server — where adding an already-present product should increment quantity rather than create a duplicate — required a check-then-upsert pattern in FastAPI. Routing between the product list and cart views without a router library was implemented using a single `view` state variable in the root component, keeping the code easy to follow. Making MongoDB's `_id` field usable on the frontend required a small conversion helper that serialises ObjectId to a plain string. Finally, configuring Vite's proxy so that all `/api` fetch calls from React are forwarded to the FastAPI server removed the need for environment-specific URLs in the frontend code.
# Shopping-cart
