from app import db  # Make sure to import db from your application
from datetime import datetime

cart_product_association = db.Table(
    'cart_product_association',
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    colors = db.Column(db.String(255))
    description = db.Column(db.String(1000))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    image = db.Column(db.String(255))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
   
   # Add relationships to Brand and Category
    brand = db.relationship('Brand', backref='products')
    category = db.relationship('Category', backref='products')
    carts = db.relationship('Cart', secondary=cart_product_association, back_populates='products')



    def __init__(self, name, price, discount, stock, colors, description, brand, category, date_added=None):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.colors = colors
        self.description = description
        self.brand = brand
        self.category = category
        self.date_added = date_added
        


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

def get_latest_products(limit=10):
    # Query the Product model to get the latest products
    latest_products = db.session.query(
        Product.name,
        Product.image,
        Brand.name.label("brand_name"),
        Product.price 
    ).join(Brand).order_by(Product.date_added.desc()).limit(limit).all()
    return latest_products



def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    print(product)  # Add this line for debugging
    return product

def add_product_to_cart(user_id, product_id):
    user_cart = Cart.query.filter_by(user_id=user_id).first()
    product = Product.query.get(product_id)

    if user_cart and product:
        user_cart.products.append(product)
        db.session.commit() 

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    products = db.relationship('Product', secondary=cart_product_association, back_populates='carts')