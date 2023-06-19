from flask_restful import Resource
from models.product import Product



class ProductResource(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self, product_id):
        """Read product"""
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found.'}, 404
        return {'id': product.id, 'color': product.color, 'weight': product.weight, 'price': product.price}, 200