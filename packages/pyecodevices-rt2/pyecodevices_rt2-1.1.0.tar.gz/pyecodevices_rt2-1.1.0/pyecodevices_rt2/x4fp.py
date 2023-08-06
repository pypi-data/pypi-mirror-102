from . import EcoDevicesRT2

from .exceptions import (
    EcoDevicesRT2RequestError,
)

from .const import (
    X4FP_GET_LINK,
    X4FP_GET_ENTRY,
    X4FP_SET_MODE_LINK,
    RESPONSE_ENTRY,
    RESPONSE_SUCCESS_VALUE,
    X4FP_TO_VALUE,
)


class X4FP:
    """Class representing the X4FP"""

    def __init__(self, ecort2: EcoDevicesRT2, module_id: int, zone_id: int) -> None:
        self._ecort2 = ecort2
        self._module_id = module_id
        self._zone_id = zone_id
        self._fp_value = (self._module_id - 1) * 4 + self._zone_id

    @property
    def mode(self) -> int:
        """Return the current X4FP mode."""
        response = self._ecort2.get(X4FP_GET_LINK)
        return X4FP_TO_VALUE[response[X4FP_GET_ENTRY % (self._module_id, self._zone_id)]]

    @mode.setter
    def mode(self, value: int):
        """Change the current X4FP mode."""
        response = self._ecort2.get(X4FP_SET_MODE_LINK % (self._fp_value, value))
        if (response[RESPONSE_ENTRY] != RESPONSE_SUCCESS_VALUE or value > 5):
            raise EcoDevicesRT2RequestError(
                "Ecodevices RT2 API error, unable to change the mode for FP extention %d, Zone %d to %d"
                % (self._module_id, self._zone_id, value))
