from . import EcoDevicesRT2

from .const import (
    POST_INSTANT_GET_LINK,
    POST_INSTANT_GET_ENTRY,
    SUBPOST_INSTANT_GET_ENTRY,
    POST_INDEX_GET_LINK,
    POST_INDEX_GET_ENTRY,
    SUBPOST_INDEX_GET_ENTRY,
    POST_INDEX_DAY_GET_LINK,
    POST_INDEX_DAY_GET_ENTRY,
    SUBPOST_INDEX_DAY_GET_ENTRY,
    POST_PRICE_GET_LINK,
    POST_PRICE_GET_ENTRY,
    SUBPOST_PRICE_GET_ENTRY,
    POST_PRICE_DAY_GET_LINK,
    POST_PRICE_DAY_GET_ENTRY,
    SUBPOST_PRICE_DAY_GET_ENTRY
)


class Post:
    """Class representing the Post or Sub-Post """

    def __init__(self, ecort2: EcoDevicesRT2, id_post: int, id_subpost: int = None) -> None:
        self._ecort2 = ecort2
        self._id_post = id_post
        self._id_subpost = id_subpost
        if (id_subpost is not None):
            self._instant_entry = SUBPOST_INSTANT_GET_ENTRY % (id_post, id_subpost)
            self._index_entry = SUBPOST_INDEX_GET_ENTRY % (id_post, id_subpost)
            self._index_day_entry = SUBPOST_INDEX_DAY_GET_ENTRY % (id_post, id_subpost)
            self._price_entry = SUBPOST_PRICE_GET_ENTRY % (id_post, id_subpost)
            self._price_day_entry = SUBPOST_PRICE_DAY_GET_ENTRY % (id_post, id_subpost)
        else:
            self._instant_entry = POST_INSTANT_GET_ENTRY % (id_post)
            self._index_entry = POST_INDEX_GET_ENTRY % (id_post)
            self._index_day_entry = POST_INDEX_DAY_GET_ENTRY % (id_post)
            self._price_entry = POST_PRICE_GET_ENTRY % (id_post)
            self._price_day_entry = POST_PRICE_DAY_GET_ENTRY % (id_post)

    @property
    def instant(self) -> float:
        """Return the instant power of post/subpost."""
        response = self._ecort2.get(POST_INSTANT_GET_LINK)
        return response[self._instant_entry]

    @property
    def index(self) -> float:
        """Return the index of post/subpost."""
        response = self._ecort2.get(POST_INDEX_GET_LINK)
        return response[self._index_entry]

    @property
    def index_day(self) -> float:
        """Return the index of the current day of post/subpost."""
        response = self._ecort2.get(POST_INDEX_DAY_GET_LINK)
        return response[self._index_day_entry]

    @property
    def price(self) -> float:
        """Return the price of post/subpost."""
        response = self._ecort2.get(POST_PRICE_GET_LINK)
        return response[self._price_entry]

    @property
    def price_day(self) -> float:
        """Return the price of the current day of post/subpost."""
        response = self._ecort2.get(POST_PRICE_DAY_GET_LINK)
        return response[self._price_day_entry]
