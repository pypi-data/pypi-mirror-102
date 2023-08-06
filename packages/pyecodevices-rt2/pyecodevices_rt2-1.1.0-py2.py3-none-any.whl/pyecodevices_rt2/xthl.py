from . import EcoDevicesRT2

from .const import (
    XTHL_GET_LINK,
    XTHL_GET_TMP_ENTRY,
    XTHL_GET_HUM_ENTRY,
    XTHL_GET_LUM_ENTRY,
)


class XTHL:
    """Class representing the XTHL"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int) -> None:
        self._ecort2 = ecort2
        self._id = id

    @property
    def temperature(self) -> bool:
        """Return the current XTHL temperature."""
        response = self._ecort2.get(XTHL_GET_LINK)
        return response[XTHL_GET_TMP_ENTRY % (self._id)]

    @property
    def humidity(self) -> bool:
        """Return the current XTHL humidity."""
        response = self._ecort2.get(XTHL_GET_LINK)
        return response[XTHL_GET_HUM_ENTRY % (self._id)]

    @property
    def luminosity(self) -> bool:
        """Return the current XTHL luminosity."""
        response = self._ecort2.get(XTHL_GET_LINK)
        return response[XTHL_GET_LUM_ENTRY % (self._id)]
