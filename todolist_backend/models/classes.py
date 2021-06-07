from typing import *
import inflect
from mongoengine.base.metaclasses import TopLevelDocumentMetaclass
from mongoengine.document import Document
from mongoengine.fields import EmbeddedDocumentField, ListField
from .embedded_comment import EmbeddedComment
from .embedded_tag import EmbeddedTag


class BaseODM(Document):
    """
    Base class for document models used by this project.
    The parent class can be swapped out at any time.

    The names of all children classes must be singular.
    For example, the name of an ODM whose collection is called `Accounts`
    must be named `Account`.
    """

    meta: Dict[str, Any] = {
        "allow_inheritance": True
    }

    @classmethod
    def collection_name(cls) -> str:
        """
        Get the collection name of a document based on its class name.
        This assumes that the name of the class is singular and is in
        English. The return value is simply the plural form of the word.

        This method uses `inflect.engine.plural` to generate the plural
        forms.

        Example
        -------

        >>> from todolist_backend.models.classes import BaseODM
        >>> class Item(BaseODM):
        ...     pass
        >>> Item.collection_name()
        Items
        >>> class Bus(BaseODM):
        ...     pass
        >>> Bus.collection_name()
        Buses
        >>> class Fish(BaseODM):
        ...     pass
        >>> Fish.collection_name()
        Fishes

        Returns
        -------
        collection_name: str
            The expected name of the collection.
        """
        return inflect.engine().plural(cls.__name__)

    
    @classmethod
    def setup_odm(cls, *args, **kwargs) -> TopLevelDocumentMetaclass:
        """
        Setup meta configs for this ODM. This class method must be called
        at least once defining a child class which inherits from `BaseODM`.

        You can overwrite data in cls.meta by specifying the desired value
        in `kwargs`.

        Example
        -------

        >>> from todolist_backend.models.classes import BaseODM
        >>> class Item(BaseODM):
        ...     pass
        >>> Item.setup_odm()
        >>> Item._meta["collection"]
        Items

        Parameters
        ----------
        *args: Tuple
            Not used as of now

        **kwargs: Dict[str, Any]
            - collection: The corresponding collection name
              default = cls.collection_name()
            - allow_inheritance: Whether to inheritance
              default = True
        """
        meta = BaseODM._meta.copy()
        meta["collection"] = kwargs.get(
            "collection", cls.collection_name()
        )
        meta["allow_inheritance"] = kwargs.get(
            "allow_inheritance", True
        )
        cls._meta = meta
        return cls


class CommentedODM(BaseODM):
    """
    A document which contains a list of comments.
    """
    comments = ListField(EmbeddedDocumentField(EmbeddedComment))


class TaggedODM(BaseODM):
    """
    A document which contains a list of tags.
    """
    tags = ListField(EmbeddedDocumentField(EmbeddedTag))
