from flask import render_template, request, flash, redirect, url_for,session
from .forms import RegistrationForm, LoginForm
from app import app,db, bcrypt
from ..models import User
from flask_login import login_user, logout_user, current_user, login_required
from ..products.models import get_latest_products, get_product_by_id, add_product_to_cart



@app.route('/')
def home():
    latest_products = get_latest_products()
    return render_template('admin/index.html', latest_products=latest_products)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    
    if request.method == 'POST':
        if form.validate():
            # Check if the email or username already exists in the database
            existing_email_user = User.query.filter_by(email=form.email.data).first()
            existing_username_user = User.query.filter_by(username=form.username.data).first()

            if existing_email_user:
                flash("Email already exists. Please choose another one.", "error")
            elif existing_username_user:
                flash("Username already exists. Please choose another one.", "error")
            else:
                # Registration is successful, add the user to the database
                hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(
                    name=form.name.data,
                    username=form.username.data,
                    email=form.email.data,
                    password=hash_password
                )

                db.session.add(user)
                db.session.commit()
                flash(f'Thank you for registering, {form.name.data}!', 'success')
                return redirect(url_for('home'))
        else:
            flash("Form is invalid. Please check the fields.", "error")

    return render_template('admin/signup.html', form=form, title="Sign up page")

from flask import render_template

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # Assuming you have a successful_login_message to pass to the template
    successful_login_message = "Login Successful"
    
    return render_template('admin.html', message=successful_login_message)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(username=form.username.data).first()
            if user:
                if user and bcrypt.check_password_hash(user.password, form.password.data):
                    session['username'] = form.username.data
                    flash(f'Welcome {form.username.data} You are loggedin')
                    return redirect(request.args.get('next') or url_for('admin'))
                else:
                    flash('Wrong Password', 'danger')
    return render_template('admin/login.html', form=form,  title='Login')


@app.route('/purchase/<string:product_id>', methods=['GET', 'POST'])
@login_required  # Requires the user to be logged in
def purchase_product(product_id):
    try:
        product_id = int(product_id)  # Convert the product_id to an integer
    except ValueError:
        flash("Invalid product ID", "danger")
        return redirect(url_for('home'))
    
    # Get the product by product_id
    product = get_product_by_id(product_id)

    if product:
        # Add the product to the user's shopping cart (you need to implement this)
        add_product_to_cart(product, current_user)

        flash("Product added to your shopping cart!", "success")
        return redirect(url_for('shopping_cart'))  # Redirect to the shopping cart page
    else:
        flash("Product not found.", "danger")
        return redirect(url_for('home'))
