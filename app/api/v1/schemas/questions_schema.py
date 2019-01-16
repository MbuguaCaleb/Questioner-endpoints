from marshmallow import Schema, fields, post_dump
from ..utils.validator import required

class QuestionSchema(Schema):

    """ schema for Question object """

    id = fields.Int(dump_only=True)
    title = fields.Str(required=False, validate=(required))
    body = fields.Str(required=True, validate=(required))
    meetup = fields.Int(required=True)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)
    votes = fields.Int(dump_only=True)



