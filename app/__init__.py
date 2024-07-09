from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

db= SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG= True,
        SECRET_KEY= 'dev',
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost/postgres',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    db.init_app(app)

    from . import myapp
    app.register_blueprint(myapp.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()

    return app