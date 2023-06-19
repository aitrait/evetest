from celery import Celery
import datetime

celery = Celery('app', broker='redis://redis:6379/0')

@celery.task
def log_order_status(order_id, status):
    with open("order_status.log","a")as logfile:
        logfile.write(f"{datetime.datetime.now()} -- Order {order_id} status changed to {status}\n")
