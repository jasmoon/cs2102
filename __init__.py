from flask import Flask, render_template
from database import get_connection, get_cursor

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'cs2102isreallyhardtoguesseh'

    # register the database commands
    import database
    database.init_app(app)

    import auth
    app.register_blueprint(auth.bp)
    import campaign
    app.register_blueprint(campaign.bp)
    import user
    app.register_blueprint(user.bp)


    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    @app.route('/')
    @app.route('/index')
    def index():
        cursor = get_cursor()
        cursor.execute("""
        SELECT c.id AS campaign_id, c.name, c.description, c.image, c.amount_requested, c.date_created,                           
        c.last_modified, ua.email AS owner_id, ua.first_name, ua.last_name, ua.profile_image, ua.description AS owner_description,
        get_total_donations(c.id) AS amount_donated,
        coalesce(ceil((get_total_donations(c.id)/c.amount_requested)*100), 0) as percentage
        FROM campaign c                                                                                                           
        INNER JOIN campaign_relation cr on c.id = cr.campaign_id                                                                
        INNER JOIN user_account ua on cr.user_account_email = ua.email WHERE cr.user_role='owner'                                                                                                                 
        ORDER BY c.date_created DESC LIMIT 3;
        """)

        campaigns = cursor.fetchall()
        return render_template("index.html", campaigns=campaigns)
    return app
