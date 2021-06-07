from mongoengine.fields import EmbeddedDocument, StringField


class EmbeddedComment(EmbeddedDocument):
    """
    A comment in a document.
    """
    content = StringField()
    name = StringField(max_length=120)
