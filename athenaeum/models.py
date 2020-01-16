from mongoengine import Document, EmbeddedDocument, fields


# Create your models here.
class Resource(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
