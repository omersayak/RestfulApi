from marshmallow import Schema, fields, validates, ValidationError
from api.app.schemas.validators import validate_name, validate_integer

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True, validate=validate_name)
    menu_item_id = fields.Int(required=True, validate=validate_integer)
    quantity = fields.Int(required=True, validate=validate_integer)

    @validates('quantity')
    def validate_quantity(self, value):
        if value < 1:
            raise ValidationError('Quantity must be at least 1')