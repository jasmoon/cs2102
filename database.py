import psycopg2
import psycopg2.extras

from flask import current_app, g


def get_connection():
    if 'connection' not in g:
        g.connection = psycopg2.connect(dbname="cs2102", user="cs2102", password="cs2102pass", host="localhost")

    return g.connection


def get_cursor():
    if 'cursor' not in g:
        g.cursor = get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)

    return g.cursor


def close_connection(e=None):
    cursor = g.pop('cursor', None)
    if cursor is not None:
        cursor.close()

    connection = g.pop('connection', None)
    if connection is not None:
        connection.close()


def init_app(app):
    app.teardown_appcontext(close_connection)