from flask import redirect, render_template, url_for, flash, request
from app import db, app
from .models import Brand, Category, Product
from .forms import AddProductForm


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        if getbrand:
            # Check if the brand with the same name already exists
            existing_brand = Brand.query.filter_by(name=getbrand).first()
            if existing_brand:
                flash(f'{getbrand} already exists', 'danger')
            else:
                brand = Brand(name=getbrand)
                db.session.add(brand)
                db.session.commit()
                flash(f'{getbrand} was successfully added', 'success')
                return redirect(url_for('addbrand'))
        else:
            flash('Brand name cannot be empty', 'danger')
    
    return render_template('products/addbrand.html', brands='brands')


@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        getcategory = request.form.get('category')
        if getcategory:
            # Check if the category with the same name already exists
            existing_category = Category.query.filter_by(name=getcategory).first()  # Use the Category model
            if existing_category:
                flash(f'{getcategory} already exists', 'danger')
            else:
                category = Category(name=getcategory)
                db.session.add(category)
                db.session.commit()
                flash(f'{getcategory} was successfully added', 'success')
                return redirect(url_for('addcategory'))
        else:
            flash('Category name cannot be empty', 'danger')
    
    return render_template('products/addbrand.html')



@app.route('/addproduct', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    brands = Brand.query.all()
    categories = Category.query.all()

    if request.method == 'POST':
        # Retrieve data from the form
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        description = form.description.data

        # Get the selected brand and category from the form
        brand_id = int(request.form.get('brand'))
        category_id = int(request.form.get('category'))

        # Retrieve brand and category objects
        brand = Brand.query.get(brand_id)
        category = Category.query.get(category_id)

        # Create a new product instance
        product = Product(name=name, price=price, discount=discount, stock=stock,
                          colors=colors, description=description, brand=brand, category=category)

        # Add the product to the database
        db.session.add(product)
        db.session.commit()

        flash('Product added successfully', 'success')
        return redirect(url_for('add_product'))

    return render_template('products/addproduct.html', title="Add Product", form=form, brands=brands, categories=categories)

