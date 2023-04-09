from api.app import db, ma

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String())
    ordered_items = db.relationship('OrderedItem', backref='order', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order

    items = ma.Nested('OrderedItemSchema', many=True)