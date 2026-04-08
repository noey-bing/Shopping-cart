// Cart Page
export default function Cart({ cart, onUpdateQuantity, onRemove, onBack }) {

  // Sum up price and quantity for every item in the cart
  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return (
    <div className="cart-page">
      <button className="btn-back" onClick={onBack}>← Back to Products</button>
      <h2 className="section-title">Your Cart</h2>

      {/* If there's nothing in the cart */}
      {cart.length === 0 ? (
        <p className="status-msg">Your cart is empty.</p>
      ) : 
        {/* If there's anything in the cart */}
        (
        <>
          {/* List all the items */}
          <div className="cart-list">
            {cart.map((item) => (
              <div className="cart-item" key={item.id}>
                <img className="cart-item-image" src={item.image} alt={item.name} />
                <div className="cart-item-info">
                  <p className="cart-item-name">{item.name}</p>
                  <p className="cart-item-price">${item.price.toFixed(2)} each</p>
                </div>
                {/* Quantity controls: − / + button, current count */}
                <div className="quantity-controls">
                  <button
                    className="qty-btn"
                    onClick={() => onUpdateQuantity(item.id, item.quantity - 1)}
                    disabled={item.quantity <= 1}
                  >
                    −
                  </button>
                  <span className="qty-display">{item.quantity}</span>
                  <button
                    className="qty-btn"
                    onClick={() => onUpdateQuantity(item.id, item.quantity + 1)}
                  >
                    +
                  </button>
                </div>
                { /* Total price per each item */}
                <p className="cart-item-subtotal">${(item.price * item.quantity).toFixed(2)}</p>
                <button className="btn-remove" onClick={() => onRemove(item.id)}>Remove</button>
              </div>
            ))}
          </div>
          { /* Total price of all items in the cart */}
          <div className="cart-total">
            <span>Total</span>
            <span>${total.toFixed(2)}</span>
          </div>
        </>
      )}
    </div>
  );
}
