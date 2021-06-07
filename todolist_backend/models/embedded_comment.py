from mongoengine.fields import EmbeddedDocumentField, StringField


class EmbeddedComment(EmbeddedDocumentField):
    """
    A comment in a document.
    """
    content = StringField()
    name = StringField(max_length=120)
