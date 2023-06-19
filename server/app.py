from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from asgiref.wsgi import WsgiToAsgi
from sqlalchemy.exc import IntegrityError
from flask_security import hash_password, http_auth_required
from security import init_security
from admin import init_admin
from api_jsonrpc import init_rpc
from db import db
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{os.environ.get("MYSQL_ROOT_PASSWORD")}@db/everest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECURITY_POST_LOGIN_VIEW'] = '/admin'
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY","zl53GX95MvMfneTuZqBimlXtlgRFtrS8XOf3DkHoNo4gkZuZhYbWFoqGuFVmpzx8")
app.config['SECURITY_PASSWORD_SINGLE_HASH'] = True
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT")


db.init_app(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()
    user_datastore = init_security(app)
    admin = init_admin(app)
    rpc = init_rpc(app)
    email = os.environ.get("ADMIN_EMAIL")
    existing_user = user_datastore.find_user(email=email)
    if not existing_user:
        password = os.environ.get("ADMIN_PASSWORD")
        user = user_datastore.create_user(email=email, password=hash_password(password))
        admin_role = user_datastore.find_or_create_role(name='admin')
        user_datastore.add_role_to_user(user, admin_role)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()



asgi_app = WsgiToAsgi(app)