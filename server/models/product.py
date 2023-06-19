from db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(7), nullable=False) #HEX
    weight = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f"Product #{self.id} ({self.color}|{self.weight}|{self.price})"
    
    def __repr__(self):
        return f'<Product {self.id}>'