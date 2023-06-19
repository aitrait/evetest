from db import db
from celery_status import log_order_status
from sqlalchemy import event

order_items = db.Table('post_tag',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('order_item_id', db.Integer, db.ForeignKey('order_item.id'), primary_key=True)
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('Address', backref=db.backref('orders', lazy=True))
    items = db.relationship('OrderItem', secondary=order_items, backref=db.backref('orders', lazy=True))
    status = db.Column(db.String(50))

    @property
    def product_list(self):
        res = {}
        for item in self.items:
            res[item.product.id] = res.get(item.product.id, 0) + 1
        return ', '.join([f"Product #{prod} ({res[prod]})" for prod in res])

    def __repr__(self):
        return f'<Order {self.id}>'

@event.listens_for(Order.status, 'set')
def on_order_status_change(target, value, oldvalue, initiator):
    if value != oldvalue:
        log_order_status(target.id, value)

class OrderItem(db.Model):
    __tablename__ = 'order_item'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', backref=db.backref('order_items', lazy=True))

    def __repr__(self):
        return f"<OrderItem {self.id} ({self.product.id}|{self.product.color}|{self.product.weight}|{self.product.price})>"
