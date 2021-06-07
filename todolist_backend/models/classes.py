from typing import *
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
        English. The resulting collection name is simply the class name
        plus the plural suffix in English ('s' or 'es'). Unfortunately, this
        is not a catch-all as English is notoriously irregular (as explained
        under `Limitations`). However, I have tried to write if cases
        for certain common cases:

        1. Normal words like `Post` and `User` will have 's' appended to the
        end.
        2. Words ending with an /s/ like sound such as words ending with
        's', 'sh', 'ch' or 'x' will have 'es' added to the back. Therefore,
        `Match` will become `Matches`.

        For more ambiguous cases, such as for words ending in 'f', you
        are going to have to specify the plural yourself. See
        `Limitations` for more info.

        Limitations
        -----------
        Because English has irregular nouns, the expected plural forms of
        some nouns cannot be formed with simple agglutination.
        For example, the plural of 'foot' is 'feet'.
        To specify a custom collection name, you can pass the name as
        a keyword argument in `cls.setup_odm` by writing:

        >>> class Man(BaseODM):
        ...     pass
        Man.setup_odm(collection="Men")

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
        name: str = cls.__name__
        # Fizzbuzz
        if name[-1] in {"s", "x"} or name[-2:] in {"sh", "ch"}:
            name += "e"
        return name + "s"

    
    @classmethod
    def setup_odm(cls, *args, **kwargs) -> Type:
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
        >>> Item.meta["collection"]
        Items

        Parameters
        ----------
        *args: Tuple
            Not used as of now

        **kwargs: Dict[str, Any]
            - collection: The corresponding collection name
        """
        meta = BaseODM._meta.copy()
        meta["collection"] = kwargs.get(
            "collection", cls.collection_name()
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
