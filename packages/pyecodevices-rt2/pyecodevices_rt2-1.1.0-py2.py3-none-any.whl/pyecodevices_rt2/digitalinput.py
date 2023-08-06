from . import EcoDevicesRT2

from .const import (
    DIGITAL_INPUT_GET_LINK,
    DIGITAL_INPUT_GET_ENTRY,
)


class DigitalInput:
    """Class representing the DigitalInput"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int) -> None:
        self._ecort2 = ecort2
        self._id = id

    @property
    def status(self) -> bool:
        """Return the current DigitalInput status."""
        response = self._ecort2.get(DIGITAL_INPUT_GET_LINK)
        return response[DIGITAL_INPUT_GET_ENTRY % (self._id)] == 1
