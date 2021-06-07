from mongoengine.fields import EmbeddedDocumentField, ListField
from .base_odm import BaseODM
from .embedded_comment import EmbeddedComment


class CommentedODM(BaseODM):
    """
    A document which contains a list of comments.
    """
    comments = ListField(EmbeddedDocumentField(EmbeddedComment))
