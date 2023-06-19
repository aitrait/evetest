from flask_security import Security, SQLAlchemyUserDatastore
from db import db
from models.user_role import User, Role

def init_security(app): 
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    return user_datastore