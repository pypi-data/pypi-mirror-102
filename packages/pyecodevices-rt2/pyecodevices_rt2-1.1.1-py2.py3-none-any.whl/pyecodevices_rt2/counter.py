from . import EcoDevicesRT2

from .const import (
    COUNTER_GET_LINK,
    COUNTER_GET_ENTRY,
    COUNTER_SET_LINK,
    RESPONSE_ENTRY,
    RESPONSE_SUCCESS_VALUE,
    PRICE_GET_LINK,
    COUNTER_PRICE_GET_ENTRY
)


class Counter:
    """Class representing the Counter"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int) -> None:
        self._ecort2 = ecort2
        self._id = id

    @property
    def value(self) -> int:
        """Return the current Counter value."""
        response = self._ecort2.get(COUNTER_GET_LINK)
        return response[COUNTER_GET_ENTRY % (self._id)]

    @value.setter
    def value(self, value: int) -> bool:
        """Modify the current Counter value."""
        response = self._ecort2.get(COUNTER_SET_LINK % (self._id, str(value)))
        return response[RESPONSE_ENTRY] == RESPONSE_SUCCESS_VALUE

    def add(self, value: int) -> bool:
        """Add a value to the current Counter value."""
        response = self._ecort2.get(COUNTER_SET_LINK % (self._id, "+%d" % value))
        return response[RESPONSE_ENTRY] == RESPONSE_SUCCESS_VALUE

    def substrat(self, value: int) -> bool:
        """Substract a value to the current Counter value."""
        response = self._ecort2.get(COUNTER_SET_LINK % (self._id, "-%d" % value))
        return response[RESPONSE_ENTRY] == RESPONSE_SUCCESS_VALUE

    @property
    def price(self) -> float:
        """Return the price of counter."""
        response = self._ecort2.get(PRICE_GET_LINK)
        return response[COUNTER_PRICE_GET_ENTRY % (self._id)]
