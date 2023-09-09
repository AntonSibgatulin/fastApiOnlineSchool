from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    surname = fields.String()
    email = fields.String()
    token = None
