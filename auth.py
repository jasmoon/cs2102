import functools
import hashlib

from flask import Blueprint, flash, g, redirect, render_template, current_app, session, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash, safe_str_cmp
from psycopg2 import IntegrityError

from database import get_connection, get_cursor
from forms import LoginForm, RegistrationForm, ResetForm, RequestResetForm

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

        error = None

        # careful now
        with connection:
            with cursor:
                try:
                    cursor.execute("""INSERT INTO 
                        user_account(email, password, first_name, last_name, address1, address2, postal_code, phone_number, 
                        profile_image, description, credit_card) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""",
                                   (
                                       form.email.data,
                                       generate_password_hash(form.password.data),
                                       form.first_name.data,
                                       form.last_name.data,
                                       form.address1.data,
                                       form.address2.data,
                                       form.postal_code.data,
                                       form.phone_number.data,
                                       form.profile_image.data,
                                       form.description.data,
                                       form.credit_card.data,
                                   )
                    )
                    return redirect(url_for('auth.login'))
                except IntegrityError as e:
                    current_app.logger.error(e)
                    error = "Email already exists!"
                except Exception as e:
                    current_app.logger.error(e)
                    error = "An error has occurred. Please try again later."
    else:
        flash(form.errors, 'error')

    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        connection = get_connection()
        cursor = get_cursor()
        error = None
        cursor.execute(
            'SELECT * FROM user_account WHERE email = %s', (email,)
        )
        user = cursor.fetchone()

        if user is None or not check_password_hash(user['password'], password):
            error = 'Incorrect email/password combination.'
        else:
            # store the user id in a new session and return to the index
            cursor.execute(
                "SELECT update_last_login(%s);", (user['id'],)
            )
            connection.commit()
            session.clear()
            session['user_id'] = user['id']

            flash("Logged in!", 'success')
            return redirect(url_for('index'))

        flash(error, 'error')

    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@bp.route('/reset/<int:uid>/<string:date_hash>', methods=('GET',))
def reset_verify(uid, date_hash):
    connection = get_connection()
    cursor = get_cursor()
    with connection:
        with cursor:
            cursor.execute("SELECT last_login FROM user_account WHERE id = %s", str(uid))
            row = cursor.fetchone()
            if safe_str_cmp(hashlib.md5(str(row['last_login']).encode()).hexdigest(), date_hash):
                session.clear()
                session['reset_user_id'] = uid
                session['reset_ok'] = True
                return redirect(url_for("auth.reset_password"))
            else:
                flash("Invalid reset link. Please try again.", 'error')
                return redirect(url_for("auth.request_reset"))


@bp.route('/reset/password', methods=('GET', 'POST'))
def reset_password():
    form = ResetForm()
    connection = get_connection()
    cursor = get_cursor()
    if session['reset_ok'] and session['reset_user_id'] is not None and form.validate_on_submit():
        with connection:
            with cursor:
                try:
                    cursor.execute("UPDATE user_account SET password = %s WHERE id = %s",
                                   (generate_password_hash(form.password.data), session['reset_user_id'])
                                   )
                    flash("Reset successful!", 'success')
                    return redirect(url_for("auth.login"))
                except Exception as e:
                    error = "Something went wrong. Please try again later"
                    current_app.logger.error(e)
                    flash(error, 'error')

    return render_template("auth/password_reset.html", form=form)


@bp.route('reset/request', methods=('GET', 'POST'))
def request_reset():
    form = RequestResetForm()
    connection = get_connection()
    cursor = get_cursor()
    if form.validate_on_submit():
        with connection:
            with cursor:
                cursor.execute("SELECT * FROM user_account WHERE email = %s", (form.email.data,))
                row = cursor.fetchone()
                if row['email'] is not None:
                    date_hash = hashlib.md5(str(row['last_login']).encode()).hexdigest()
                    import smtplib
                    from email.mime.text import MIMEText

                    message = MIMEText("""You've requested a password change! Head over to %s""" % \
                              (request.host + url_for("auth.reset_verify", uid=row['id'], date_hash=date_hash)))
                    message['Subject'] = "Password reset request"
                    message['From'] = "cs2102@sute.jp"
                    message['To'] = row['email']

                    smtp = smtplib.SMTP(host="127.0.0.1", port=8080)
                    smtp.sendmail("cs2102@sute.jp", row['email'], message.as_string())

                    current_app.logger.info(message)
                    return render_template("auth/request_reset.html", hash=date_hash)

    return render_template("auth/request_reset.html", form=form)
