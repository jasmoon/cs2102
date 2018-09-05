from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, URL, Optional
from wtforms import StringField, PasswordField, HiddenField


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(), EqualTo('password', message="Your passwords do not match!")])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    address1 = StringField('Address', validators=[DataRequired()])
    address2 = StringField('Address 2', validators=[Optional()])
    postal_code = StringField('Postal Code', validators=[])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    profile_image = StringField('Profile Image', validators=[DataRequired(), URL()])
    description = StringField('Short bio', validators=[DataRequired()])
    stripe_token = HiddenField("Stripe Token", validators=[DataRequired()])


