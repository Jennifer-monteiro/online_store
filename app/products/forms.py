from wtforms import StringField, FloatField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, Optional, Length
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class AddProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0.01)])
    discount = IntegerField('Discount Percentage', validators=[Optional(), NumberRange(min=0, max=100)])
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
    colors = StringField('Available Colors', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Product Description', validators=[DataRequired()])
    image = FileField('Product Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])

