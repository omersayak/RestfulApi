from marshmallow import Schema, fields, validates, ValidationError
from api.app.schemas.validators import validate_name, validate_email

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate_name)
    email = fields.Email(required=True, validate=validate_email)

    @validates('username')
    def validate_username_length(self, value):
        if len(value) < 3:
            raise ValidationError('Username must be at least 3 characters')
        elif len(value) > 25:
            raise ValidationError('Username must be no more than 25 characters')