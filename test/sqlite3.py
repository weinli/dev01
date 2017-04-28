import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

DATABASE = '/software/PycharmProjects/test/db/flaskr.db'

def connect_db():
    return sqlite3.connect_db(DATABASE)

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == '__main__':



