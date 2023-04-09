from api.app import db, ma

class OrderedItem(db.Model):
    __tablename__ = 'ordered_item'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    quantity = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class OrderedItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderedItem

    menu = ma.Nested('MenuSchema')