from db import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(50), nullable=False)
    additional = db.Column(db.String(50), nullable=True)

    def __str__(self):
        return ", ".join([self.country, self.city, self.street, self.additional])
    
    def __repr__(self):
        return f'<Address {self.id}>'