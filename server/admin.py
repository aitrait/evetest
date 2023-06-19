from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import login_required
from flask import redirect, url_for
from models.product import Product
from models.address import Address
from models.user_role import User, Role
from models.order import Order, OrderItem
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from db import db
from flask_security import current_user


class AddressAdminView(ModelView):
    column_filters = ('country', 'city', 'street')

    column_searchable_list = ('country', 'city', 'street')
    column_filters = ('country', 'city', 'street')

    def scaffold_form(self):
        form_class = super(AddressAdminView, self).scaffold_form()
        form_class.country = StringField('Country', validators=[DataRequired()])
        form_class.city = StringField('City', validators=[DataRequired()])
        form_class.street = StringField('Street', validators=[DataRequired()])
        return form_class

class OrderView(ModelView):
    column_list = ('id', 'address', 'status', 'product_list')
    
class OrderItemView(ModelView):
    column_list = ('id', 'product')
    column_sortable_list = ('id', 'product')
    form_columns = ['product']

class ProtectedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

class ProtectedAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated
    def _handle_view(self, name):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

def init_admin(app):


    @login_required
    @app.route('/login')
    def login():
        return redirect('/admin')

    admin = Admin(app, name='Admin', template_mode='bootstrap3', index_view=ProtectedAdminIndexView())
    admin.add_view(ProtectedView(Product, db.session))
    admin.add_view(ProtectedView(User, db.session))
    admin.add_view(ProtectedView(Role, db.session))
    admin.add_view(OrderItemView(OrderItem, db.session))
    admin.add_view(AddressAdminView(Address, db.session))
    admin.add_view(OrderView(Order, db.session))