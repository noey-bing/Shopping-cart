export default function Cart({ cart, onUpdateQuantity, onRemove, onBack }) {
  // Calculate the total price of all items in the cart
  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return (
    <div className="cart-page">
      <button className="btn-back" onClick={onBack}>
        ← Back to Products
      </button>
      <h2 className="section-title">Your Cart</h2>

      {cart.length === 0 ? (
        <p className="empty-msg">Your cart is empty.</p>
      ) : (
        <>
          <div className="cart-list">
            {cart.map((item) => (
              <div className="cart-item" key={item.id}>
                <img
                  className="cart-item-image"
                  src={item.image}
                  alt={item.name}
                />
                <div className="cart-item-info">
                  <p className="cart-item-name">{item.name}</p>
                  <p className="cart-item-price">${item.price.toFixed(2)} each</p>
                </div>

                {/* Quantity controls: minus, number input, plus */}
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

                <p className="cart-item-subtotal">
                  ${(item.price * item.quantity).toFixed(2)}
                </p>

                <button
                  className="btn-remove"
                  onClick={() => onRemove(item.id)}
                >
                  Remove
                </button>
              </div>
            ))}
          </div>

          {/* Order total */}
          <div className="cart-total">
            <span>Total</span>
            <span>${total.toFixed(2)}</span>
          </div>
        </>
      )}
    </div>
  );
}
