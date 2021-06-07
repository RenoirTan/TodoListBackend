from mongoengine.document import EmbeddedDocument
from mongoengine.fields import StringField


class EmbeddedTag(EmbeddedDocument):
    """
    A tag in a document.
    """
    name = StringField(max_length=120)
