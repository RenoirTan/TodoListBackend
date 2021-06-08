from mongoengine.fields import EmbeddedDocument, DateTimeField, BooleanField


class EmbeddedCompletion(EmbeddedDocument):
    """
    An embedded part of a document which specifies when an action has
    been completed or not and when it has been completed.
    """
    completedDate = DateTimeField()
    completed = BooleanField(required=True)
