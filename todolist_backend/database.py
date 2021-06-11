from typing import *
from mongoengine import connect
from .info import DBSERVER_CONFIGS, MONGOENGINE_ALIAS


__all__ = ["iter_mongo_uris", "init"]


def iter_mongo_uris(configs: Dict[str, Any]) -> Generator[str, str, None]:
    """
    Iterate through all combinations of MongoDB URIs. The resulting URIs
    can be used to attempt a connection to the cluster.

    Example
    -------

    >>> from todolist_backend.info import DBSERVER_CONFIGS
    >>> from todolist_backend.database import iter_mongo_uris
    >>> for uri in iter_mongo_uris(DBSERVER_CONFIGS):
    >>>     print(uri)
    mongodb+srv://your-username:your-password@cluster-name.10101.mongodb.net

    Parameters
    ----------
    configs: Dict[str, Any]
        The database server configuration file used to connect to the cluster.
    
    Yields
    ------
    uri: str
        A fully-formed URI that can be used to connect to a MongoDB cluster.
    """
    uri_format: str = configs["uriformat"]
    cluster_url: str = configs["clusterurl"]
    database: str = configs["database"]
    for credential in configs["credentials"]:
        yield uri_format.format(
            clusterurl=cluster_url,
            database=database,
            username=credential["username"],
            password=credential["password"]
        )


def calm_init() -> Tuple[bool, List[Exception]]:
    """
    Initialise the database connection.

    Returns
    -------
    ok, exceptions: Tuple[bool, List[Exception]]
        If one of the connection attempts was successful, `ok` will be True
    """
    exceptions: List[Exception] = []
    for uri in iter_mongo_uris(DBSERVER_CONFIGS):
        try:
            print("Trying {0}".format(uri))
            connect(alias=MONGOENGINE_ALIAS, host=uri)
        except Exception as e:
            exceptions.append(e)
            continue
        else:
            print("Connection successful!")
            return True, exceptions
    return False, exceptions


def panic_init():
    """
    Initialise the database connection but panic if no connection attempt
    was successful.

    Raises
    ------
    ValueError
        If no connection attempt was successful.
    """
    ok, exceptions = calm_init()
    if not ok:
        raise ValueError(exceptions)
