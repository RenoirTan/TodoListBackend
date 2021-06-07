from todolist_backend.models.classes import BaseODM


class Example(BaseODM):
    pass


def test_collection_name():
    assert Example.collection_name() == "Examples"


def test_setup_odm():
    Example.setup_odm(collection="CompletelyArbitraryName")
    assert Example._meta["collection"] == "CompletelyArbitraryName"
