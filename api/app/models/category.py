from api.app import db,ma 


class Category(db.model):
    __tablename__= 'category'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

       