import { useState, useEffect } from "react";
import ProductList from "./ProductList";
import Cart from "./Cart";

// All API requests go through Vite's proxy (/api → http://localhost:8000)
const API = "/api";

export default function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [view, setView] = useState("products"); // "products" or "cart"
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch data from both products and cart on first render
  useEffect(() => {
    async function loadData() {
      try {
        await Promise.all([fetchProducts(), fetchCart()]);
      } catch {
        setError("Could not connect to the server. Make sure the backend is running.");
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, []);

  // Fetch data from products
  async function fetchProducts() {
    const res = await fetch(`${API}/products`);
    const data = await res.json();
    setProducts(data);
  }

  // Fetch data from cart
  async function fetchCart() {
    const res = await fetch(`${API}/cart`);
    const data = await res.json();
    setCart(data);
  }

  // API for adding item to cart
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
    fetchCart();
  }

  // API for updating item quantity in the cart
  async function updateQuantity(itemId, quantity) {
    await fetch(`${API}/cart/${itemId}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ quantity }),
    });
    fetchCart();
  }

  // API for deleting the item from the cart
  async function removeFromCart(itemId) {
    await fetch(`${API}/cart/${itemId}`, { method: "DELETE" });
    fetchCart();
  }

  // Total number of individual items added in cart
  const cartCount = cart.reduce((sum, item) => sum + item.quantity, 0);


  // Loading message based on the connection status
  if (loading) return <p className="status-msg">Loading...</p>;
  if (error) return <p className="status-msg error">{error}</p>;


  // Startup header and page (products view)
  return (
    <div>
      <header className="header">
        <h1 className="logo" onClick={() => setView("products")}>Soyeon's Cart</h1>
        <button className="cart-btn" onClick={() => setView("cart")}>
          Cart
          {cartCount > 0 && <span className="cart-badge">{cartCount}</span>} 
        </button>
      </header>
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
