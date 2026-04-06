import { useState, useEffect } from "react";
import ProductList from "./ProductList";
import Cart from "./Cart";

const API = "/api";

export default function App() {
  // products: list fetched from the database
  const [products, setProducts] = useState([]);
  // cart: list of items currently in the cart
  const [cart, setCart] = useState([]);
  // view: which page to show — "products" or "cart"
  const [view, setView] = useState("products");

  // Load products and cart when the app first opens
  useEffect(() => {
    fetchProducts();
    fetchCart();
  }, []);

  async function fetchProducts() {
    const res = await fetch(`${API}/products`);
    const data = await res.json();
    setProducts(data);
  }

  async function fetchCart() {
    const res = await fetch(`${API}/cart`);
    const data = await res.json();
    setCart(data);
  }

  // Add a product to the cart (or increase its quantity if already there)
  async function addToCart(product) {
    await fetch(`${API}/cart`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        product_id: product.id,
        name: product.name,
        price: product.price,
        image: product.image,
      }),
    });
    fetchCart(); // refresh cart after adding
  }

  // Change the quantity of an item already in the cart
  async function updateQuantity(itemId, quantity) {
    await fetch(`${API}/cart/${itemId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ quantity }),
    });
    fetchCart();
  }

  // Remove an item from the cart
  async function removeFromCart(itemId) {
    await fetch(`${API}/cart/${itemId}`, { method: "DELETE" });
    fetchCart();
  }

  // Total number of items across all cart entries
  const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);

  return (
    <div>
      {/* ── Header ───────────────────────────────────── */}
      <header className="header">
        <h1 className="logo" onClick={() => setView("products")}>
          ShopCart
        </h1>
        <button className="cart-btn" onClick={() => setView("cart")}>
          🛒 Cart
          {cartCount > 0 && <span className="cart-badge">{cartCount}</span>}
        </button>
      </header>

      {/* ── Main content ─────────────────────────────── */}
      <main className="main">
        {view === "products" ? (
          <ProductList products={products} onAddToCart={addToCart} />
        ) : (
          <Cart
            cart={cart}
            onUpdateQuantity={updateQuantity}
            onRemove={removeFromCart}
            onBack={() => setView("products")}
          />
        )}
      </main>
    </div>
  );
}
