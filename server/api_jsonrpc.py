from flask_jsonrpc import JSONRPC
from flask_security import http_auth_required
from resources.order import OrderResource
from flask_security.decorators import http_auth_required
from db import db
from flask.wrappers import Response
def init_rpc(app):
    jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)
    @http_auth_required
    def order_info(order_id):
        resource = OrderResource(db=db)
        return resource.get(order_id)
    
    @jsonrpc.method('order.get_order_info', validate=True)
    def get_order_info(order_id:int)->dict:
        result = order_info(order_id)
        if type(result)==Response:
            return {"message":"User is not authenticated"}
        elif type(result)==tuple:
            return result[0]
        return order_info(order_id)
