# E-Commerce Shopping Cart

This project aims to build a single-page web application where users can manipulate a shopping cart including browsing, adding, adjusting quantities, and removing items. All user behaviour is processed without any page reloads.

---

## Technical Stack

| Layer      | Technology                       |
|------------|----------------------------------|
| Frontend   | React 18 (Vite)                  |
| Styling    | CSS (single stylesheet)          |
| Routing    | React state toggle (no router)   |
| Backend    | Python + FastAPI                 |
| Database   | MongoDB with PyMongo             |
| Deployment | Local                            |

---

## Features

- Responsive product grid loaded from the database
- Single-page — no full page reloads
- Loading message on startup page; error message if the backend is unreachable
- Manipulate a shopping cart
    * Add a product to the cart (increments quantity if already present)
    * Adjust item quantity with +/− buttons
    * Remove an item from the cart with one click
- Cart item count badge updates live in the header
- Cart total price automatically recalculates


---

## Folder Structure

```
/
├── frontend/              React frontend (Vite)
│   ├── src/
│   │   ├── App.jsx          Root component — state, API calls, loading/error
│   │   ├── ProductList.jsx  Product grid view
│   │   ├── Cart.jsx         Cart view
│   │   └── index.css        All styles
│   └── index.html           Single HTML entry point
│
├── backend/               FastAPI backend
│   ├── main.py              All API routes (products + cart CRUD)
│   ├── database.py          MongoDB connection
│   └── requirements.txt     Package list needed to be installed using pip
│
├── database/
│   └── seed_products.py     Run this to load products into MongoDB
│
└── README.md
```

---

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.10+
- MongoDB running locally on port 27017

### macOS

**1. Start MongoDB**
```bash
brew services start mongodb-community
```

**2. Set up and run the backend**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**3. Seed the database (first time only)**
```bash
python3 database/seed_products.py
```

**4. Run the frontend** (new terminal tab)
```bash
cd frontend
npm install
npm run dev
```

### Windows

**1. Start MongoDB**
```powershell
net start MongoDB
```

**2. Set up and run the backend**
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**3. Seed the database (first time only)**
```powershell
python database\seed_products.py
```

**4. Run the frontend** (new terminal window)
```powershell
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000` in your browser.

---

## API Endpoints

| Method | Endpoint       | Description                   |
|--------|----------------|-------------------------------|
| GET    | `/products`    | Get all products              |
| GET    | `/cart`        | Get all cart items            |
| POST   | `/cart`        | Add a product to the cart     |
| PUT    | `/cart/{id}`   | Update cart item quantity     |
| DELETE | `/cart/{id}`   | Remove an item from the cart  |

---

## A Summary of Challenges Overcome

To be honest, I had challenges on each side: frontend, backend, and database side. 

On the frontend and database side, the hardest part was making sure the cart view always in sync with the database whenever user behaviour occurs such as adding, updating, or deleting items. So, I re-fetch the data every time something gets added, updated, or deleted so that the UI always reflects real data. 

On the backend, when someone adds a product that's already in the cart, check-before-insert pattern was needed to increment quantity instead of accidentaly creating a duplicate row. 

On the database, I need to turn MongoDB's `_id` field into a normal string because that field (ObjectId object) can't be sent directly to the frontend. So, I used a small helper function to turn it into a plain string for every response.

For switching between the product list and the cart with a router library, I handled it with a single `view` state variable, which kept the component tree simple. Proxying frontend fetch calls through Vite to the FastAPI server meant the production URL never had to be hardcoded anywhere in the React code.