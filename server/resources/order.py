from flask_restful import Resource
from models.order import Order
from .product import ProductResource


class OrderResource(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self, order_id: int) -> dict:
        order = Order.query.get(order_id)
        if not order:
            return {'message': 'Order not found'}, 404
        order_data = {
            'id': order.id,
            'address': str(order.address),
            'items': [{"id":item.id,"product":ProductResource(db=self.db).get(product_id=item.product.id)[0]} for item in order.items],
            'products_list': order.product_list,
            'status': order.status
        }
        return order_data