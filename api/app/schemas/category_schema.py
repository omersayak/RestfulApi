from marshmallow import Schema, fields, validates, ValidationError
from api.app.schemas.validators import validate_name, validate_description

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate_name)
    description = fields.Str(validate=validate_description)

    @validates('name')
    def validate_unique_name(self, value):
        if len(value) > 30:
            raise ValidationError('Name must be no more than 30 characters')