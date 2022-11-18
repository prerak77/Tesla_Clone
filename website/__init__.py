from flask import Flask
from .models import *

def create_app():
    app = Flask(__name__)
    app.config['SECURITY KEY'] = 'abc'
    from .views import views

    # MYSQL CODE
    create_database()
    create_table_car_1()
    create_table_user()

    app.register_blueprint(views, url_prefix='/')
    return app