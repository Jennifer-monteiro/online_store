from app import db  # Make sure to import db from your application

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    colors = db.Column(db.String(255))
    description = db.Column(db.String(255))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
   
   # Add relationships to Brand and Category
    brand = db.relationship('Brand', backref='products')
    category = db.relationship('Category', backref='products')

    def __init__(self, name, price, discount, stock, colors, description, brand, category):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.colors = colors
        self.description = description
        self.brand = brand
        self.category = category
        


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

