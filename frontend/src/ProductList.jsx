// Product Page
export default function ProductList({ products, onAddToCart }) {

  // if there's no product
  if (products.length === 0) {
    return <p className="status-msg">No products found. Run seed_products.py to add products.</p>;
  }

  return (
    <div>
      <h2 className="section-title">All Products</h2>
      {/* Responsive grid — columns adjust based on screen width */}
      <div className="product-grid">
        {products.map((product) => (
          <div className="product-card" key={product.id}>
            <img className="product-image" src={product.image} alt={product.name} />
            <div className="product-info">
              <h3 className="product-name">{product.name}</h3>
              <p className="product-desc">{product.description}</p>
              <div className="product-footer">
                <span className="product-price">${product.price.toFixed(2)}</span>
                <button className="btn-primary" onClick={() => onAddToCart(product)}>
                  Add to Cart
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
