from . import EcoDevicesRT2

from .const import (
    INDEX_GET_LINK,
    TOROID_GET_CONSUMPTION_ENTRY,
    TOROID_GET_PRODUCTION_ENTRY,
    TOROID_GET_ENTRY,
    PRICE_GET_LINK,
    TOROID_PRICE_GET_CONSUMPTION_ENTRY,
    TOROID_PRICE_GET_PRODUCTION_ENTRY,
    TOROID_PRICE_GET_ENTRY
)

from .exceptions import (
    EcoDevicesRT2RequestError,
)


class Toroid:
    """Class representing the Toroid"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int, default_value_is_consumption: bool = True) -> None:
        self._ecort2 = ecort2
        self._id = id

        self._default_value_is_consumption = default_value_is_consumption
        self._toroid_get_entry = TOROID_GET_ENTRY % (self._id)
        self._toroid_price_get_entry = TOROID_PRICE_GET_ENTRY % (self._id)
        self._toroid_get_entry_consumption = None
        self._toroid_get_entry_production = None
        self._toroid_price_get_entry_consumption = None
        self._toroid_price_get_entry_production = None
        if (self._id <= 4):
            self._toroid_get_entry_consumption = TOROID_GET_CONSUMPTION_ENTRY % (self._id)
            self._toroid_get_entry_production = TOROID_GET_PRODUCTION_ENTRY % (self._id)
            self._toroid_price_get_entry_consumption = TOROID_PRICE_GET_CONSUMPTION_ENTRY % (self._id)
            self._toroid_price_get_entry_production = TOROID_PRICE_GET_PRODUCTION_ENTRY % (self._id)
            if (self._default_value_is_consumption):
                self._toroid_get_entry = self._toroid_get_entry_consumption
                self._toroid_price_get_entry = self._toroid_price_get_entry_consumption
            else:
                self._toroid_get_entry = self._toroid_get_entry_production
                self._toroid_price_get_entry = self._toroid_price_get_entry_production

    @property
    def value(self) -> float:
        """Return the current Toroid status."""
        response = self._ecort2.get(INDEX_GET_LINK)
        return response[self._toroid_get_entry]

    @property
    def consumption(self) -> float:
        """Return the current Toroid value for consumtion, if id is between 1 and 4."""
        if (self._id > 4):
            raise EcoDevicesRT2RequestError("Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have consumption value." % self._id)
        response = self._ecort2.get(INDEX_GET_LINK)
        return response[self._toroid_get_entry_consumption]

    @property
    def production(self) -> float:
        """Return the current Toroid value for production, if id is between 1 and 4."""
        if (self._id > 4):
            raise EcoDevicesRT2RequestError("Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have production value." % self._id)
        response = self._ecort2.get(INDEX_GET_LINK)
        return response[self._toroid_get_entry_production]

    @property
    def price(self) -> float:
        """Return the price of toroid."""
        response = self._ecort2.get(PRICE_GET_LINK)
        return response[self._toroid_price_get_entry]

    @property
    def consumption_price(self) -> float:
        """Return the current Toroid price for consumtion, if id is between 1 and 4."""
        if (self._id > 4):
            raise EcoDevicesRT2RequestError("Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have price consumption value." % self._id)
        response = self._ecort2.get(PRICE_GET_LINK)
        return response[self._toroid_price_get_entry_consumption]

    @property
    def production_price(self) -> float:
        """Return the current Toroid price for production, if id is between 1 and 4."""
        if (self._id > 4):
            raise EcoDevicesRT2RequestError("Ecodevices RT2 API error, toroid (id=%d) with id>4 does not have price production value." % self._id)
        response = self._ecort2.get(PRICE_GET_LINK)
        return response[self._toroid_price_get_entry_production]
