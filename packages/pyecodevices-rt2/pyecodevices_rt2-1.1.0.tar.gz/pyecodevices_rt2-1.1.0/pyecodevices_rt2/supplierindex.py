from . import EcoDevicesRT2, AbstractSensor

from .const import (
    INDEX_GET_LINK,
    INDEX_SUPPLIER_GET_ENTRY,
    PRICE_SUPPLIER_GET_LINK,
    PRICE_SUPPLIER_GET_ENTRY
)


class SupplierIndex(AbstractSensor):
    """Class representing the SupplierIndex """

    def __init__(self, ecort2: EcoDevicesRT2, id: int) -> None:
        super(SupplierIndex, self).__init__(
            ecort2, id,
            INDEX_GET_LINK, INDEX_SUPPLIER_GET_ENTRY)

    @property
    def price(self) -> float:
        """Return the price of supplier index."""
        response = self._ecort2.get(PRICE_SUPPLIER_GET_LINK)
        return response[PRICE_SUPPLIER_GET_ENTRY % (self._id)]
