from flask import Flask, render_template


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = b'cs2102isreallyhardtoguesseh'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register the database commands
    import database
    database.init_app(app)

    import auth
    app.register_blueprint(auth.bp)
    import campaign
    app.register_blueprint(campaign.bp)

    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    @app.route('/index')
    def index():
        return render_template('base.html')

    return app
