import logging
from pyunsplash import PyUnsplash


def getImages(client_id, topic='art'):
    py_un = PyUnsplash(api_key=client_id)
    logging.getLogger("pyunsplash").setLevel(logging.DEBUG)
    # retrieve 4 random photos, which are featured, and tagged as "dog"
    return py_un.photos(type_='random', count=1, featured=True, query=topic)
