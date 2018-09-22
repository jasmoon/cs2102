from flask import current_app, g, Blueprint, session, render_template, redirect, url_for, flash

from auth import login_required
from database import get_connection, get_cursor
from forms import EditUserProfile


bp = Blueprint('user_profile', __name__, url_prefix='/user_profile')


@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_user_profile(id):
    connection = get_connection()   # create a DB session
    cursor = get_cursor()           # allows interaction with DB by executing and fetching
    cursor.execute("""SELECT up.first_name, up.last_name, up.address1, up.address2, up.postal_code, up.phone_number, up.profile_image, up.description, up.credit_card
                      FROM user_profile up
                      WHERE id=%s;""", (id,))
    curr_user = cursor.fetchone() # fetch one row from the cursor.execute()
    curr_user = dict(zip(list(curr_user._index.keys()), list(curr_user)))
    current_app.logger.info(curr_user)
    form = EditUserProfile(**curr_user)

    if form.validate_on_submit():
        try:
            with connection:
                with cursor:
                    cursor.execute("""UPDATE user_profile
                                      SET (first_name, last_name, address1, address2, postal_code, 
                                           phone_number, profile_image, description, credit_card) =  
                                          (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                      WHERE id=%s;""", (form.first_name.data, form.last_name.data, form.address1.data,
                                                        form.address2.data, form.postal_code.data, form.phone_number.data,
                                                        form.profile_image.data, form.description.data, form.credit_card.data, id))
            flash("Successfully updated!", 'success')
            return redirect(url_for("user_profile.view_user_profile", id=id))
        except Exception as e:
            current_app.logger.error(e)
    else:
        flash("Not working")

    return render_template("user_profile/edit.html", form=form, id=id)


@bp.route('/<int:id>', methods=('GET', 'POST'))
@login_required
def view_user_profile(id) :
    cursor = get_cursor()           # allows interaction with DB by executing and fetching
    cursor.execute("""SELECT up.first_name, up.last_name, up.address1, up.address2, up.postal_code, up.phone_number, up.profile_image, up.description, up.credit_card
                      FROM user_profile up
                      WHERE id=%s;""", (id,))
    curr_user = cursor.fetchone() # fetch one row from the cursor.execute()
    curr_user = dict(zip(list(curr_user._index.keys()), list(curr_user)))
    current_app.logger.info(curr_user)

    return render_template("user_profile/user_profile.html", user_info=curr_user, id=id)

