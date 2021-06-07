from mongoengine.fields import EmbeddedDocumentField, ListField
from .base_odm import BaseODM
from .embedded_tag import EmbeddedTag


class TaggedODM(BaseODM):
    """
    A document which contains a list of tags.
    """
    tags = ListField(EmbeddedDocumentField(EmbeddedTag))
