from marshmallow import Schema, fields, validates, ValidationError
from api.app.schemas.validators import validate_name, validate_price, validate_url

class MenuSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate_name)
    price = fields.Float(required=True, validate=validate_price)
    url = fields.Str(required=True, validate=validate_url)

    @validates('url')
    def validate_unique_url(self, value):
        if ' ' in value:
            raise ValidationError('Url should not contain spaces')