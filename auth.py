import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from psycopg2 import IntegrityError

from database import get_connection, get_cursor
from forms import LoginForm, RegistrationForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        get_cursor().execute(
            'SELECT * FROM user_account WHERE id = %s', (user_id,)
        )
        g.user = get_cursor().fetchone()


@bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        connection = get_connection()
        cursor = get_cursor()

        # start a transaction to create both the user and its user profile
        error = None

        # careful now
        with connection:
            with cursor:
                try:
                    print("trying to insert user")
                    cursor.execute("INSERT INTO user_account(email, password) VALUES (%s, %s);",
                                   (form.email.data, generate_password_hash(form.password.data)))
                    print("trying to insert profile")
                    cursor.execute("""INSERT INTO 
                        user_profile(first_name, last_name, address1, address2, postal_code, phone_number, 
                        profile_image, description, stripe_token, user_account_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,(SELECT id FROM user_account WHERE email=%s));""",
                                   (
                                       form.first_name.data,
                                       form.last_name.data,
                                       form.address1.data,
                                       form.address2.data,
                                       form.postal_code.data,
                                       form.phone_number.data,
                                       form.profile_image.data,
                                       form.description.data,
                                       form.stripe_token.data,
                                       form.email.data
                                   )
                    )
                    return redirect(url_for('auth.login'))
                except IntegrityError:
                    error = "Email already exists!"
                except Exception as e:
                    print(e)
                    error = "An error has occurred. Please try again later."

        flash(error)
    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        cursor = get_cursor()
        error = None
        cursor.execute(
            'SELECT * FROM user_account WHERE email = %s', (email,)
        )
        user = cursor.fetchone()

        if user is None:
            error = 'Email doesn\'t exist'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session['user_id'] = user['id']
            flash("logged in")
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for('index'))