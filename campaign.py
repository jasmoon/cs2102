import stripe
from flask import current_app, g, Blueprint, session, render_template, redirect, url_for, flash
from decimal import Decimal

from auth import login_required
from database import get_connection, get_cursor
from forms import CampaignCreationForm, CampaignEditForm, DonationForm


bp = Blueprint('campaign', __name__, url_prefix='/campaign')
stripe.api_key = "sk_test_aWtKLQym8glXQBvFQrfYvI1Z"


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_campaign():
    form = CampaignCreationForm()
    connection = get_connection()
    cursor = get_cursor()
    if form.validate_on_submit():
        try:
            with connection:
                with cursor:
                    cursor.execute("""INSERT INTO campaign(name, description, image, amount_requested) 
                                      VALUES (%s, %s, %s, %s) RETURNING id;""",
                                   (form.name.data, form.description.data, form.image.data, form.amount_requested.data))

                    id = cursor.fetchone()[0]

                    cursor.execute("""INSERT INTO campaign_relation(user_account_id, campaign_id, user_role) 
                                      VALUES (%s, %s, %s); """,
                                   (session['user_id'], id, 'owner'))
                    return redirect(url_for("campaign.view_campaign", id=id))
        except Exception as e:
            current_app.logger.error(e)

    return render_template("campaign/create.html", form=form)


@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_campaign(id):
    connection = get_connection()
    cursor = get_cursor()
    cursor.execute("""SELECT name, description, image, amount_requested FROM campaign WHERE id=%s;""",(id,))
    curr_campaign = cursor.fetchone()
    curr_campaign['amount_requested'] = Decimal(curr_campaign['amount_requested'].replace(",","").replace("$",""))
    curr_campaign = dict(zip(list(curr_campaign._index.keys()), list(curr_campaign)))
    current_app.logger.info(curr_campaign)
    form = CampaignEditForm(**curr_campaign)
    owner_id = None

    try:
        cursor.execute("""SELECT user_account_id FROM campaign_relation WHERE campaign_id=%s AND user_role='owner'""",
                       (id,))
        owner_id = cursor.fetchone()[0]

    except Exception as e:
        current_app.logger.error(e)

    if owner_id != session['user_id']:
        flash("You cannot edit a campaign you don't own!", 'error')
        return redirect(url_for("campaign.view_campaign", id))

    if form.validate_on_submit():
        try:
            with connection:
                with cursor:
                    cursor.execute("""UPDATE campaign SET (name, description, image, amount_requested) =  
                                      (%s, %s, %s, %s) WHERE id=%s;""",
                                   (form.name.data, form.description.data, form.image.data,
                                    form.amount_requested.data, form.campaign_id.data))
            flash("Succesully updated!", 'success')
            return redirect(url_for("campaign.view_campaign", id=id))
        except Exception as e:
            current_app.logger.error(e)

    return render_template("campaign/edit.html", form=form, id=id)


@bp.route('/<int:id>', methods=('GET', 'POST'))
def view_campaign(id):
    connection = get_connection()
    cursor = get_cursor()
    form = DonationForm()
    campaign = None
    try:
        cursor.execute("""
            SELECT c.id AS campaign_id, c.name, c.description, c.image, c.amount_requested, c.date_created, 
            c.last_modified, up.id AS owner_id, up.first_name, up.last_name, up.profile_image, up.description 
            FROM campaign c
            INNER JOIN campaign_relation cr on c.id = cr.campaign_id
            INNER JOIN user_account ua on cr.user_account_id = ua.id
            INNER JOIN user_profile up on ua.id = up.user_account_id where c.id = %s;
        """, (id,))
        campaign = cursor.fetchone()
    except Exception as e:
        current_app.logger.error(e)

    if form.validate_on_submit():
        try:
            connection = get_connection()
            cursor = get_cursor()
            with connection:
                with cursor:
                    cursor.execute("""
                        SELECT stripe_token FROM user_profile WHERE user_account_id=%s
                    """, (session['user_id'],))

                    s = cursor.fetchone()[0]
                    customer = stripe.Customer.retrieve(s)
                    charge = stripe.Charge.create(
                        amount=100,
                        currency="sgd",
                        source=customer['default_source'],
                        customer=customer['id']
                    )

                    cursor.execute("""
                        INSERT INTO stripe_transaction(stripe_transaction_id, amount) 
                        VALUES (%s, %s) RETURNING id;
                    """, (charge['id'], form.amount.data))

                    transaction_id = cursor.fetchone()[0]

                    cursor.execute("""
                        INSERT INTO campaign_relation(user_account_id, campaign_id, transaction_id, user_role) 
                        VALUES (%s, %s, %s, %s)   
                    """, (id, form.campaign_id.data, transaction_id, 'pledged'))

                    flash('Successfully donated!', 'success')
        except Exception as e:
            current_app.logger.error(e)
            flash(e, 'error')

    flash(form.errors, 'error')
    return render_template("campaign/campaign.html", form=form, campaign=campaign)

