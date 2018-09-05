from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, URL, Optional, NumberRange
from wtforms import StringField, PasswordField, HiddenField, TextAreaField, DecimalField


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
    description = TextAreaField('Short Bio', validators=[DataRequired()])
    stripe_token = HiddenField("Stripe Token", validators=[DataRequired()])


class ResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(), EqualTo('password', message="Your passwords do not match!")])


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])


class CampaignCreationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Short bio', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired(), URL()])
    amount_requested = DecimalField('Amount Requested', places=2, validators=[DataRequired(),
                                                        NumberRange(min=0, message="Amount must be more than %(min)s")])


class CampaignEditForm(FlaskForm):
    campaign_id = HiddenField("Campaign ID", validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Short bio', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired(), URL()])
    amount_requested = DecimalField('Amount Requested', places=2, validators=[DataRequired(),
                                                                              NumberRange(min=0, message="Amount must be more than %(min)s")])


class DonationForm(FlaskForm):
    campaign_id = HiddenField("Campaign ID", validators=[DataRequired()])
    amount = DecimalField('Amount Donating', places=2, validators=[DataRequired(),
                                                       NumberRange(min=0, message="Amount must be more than %(min)s")])
