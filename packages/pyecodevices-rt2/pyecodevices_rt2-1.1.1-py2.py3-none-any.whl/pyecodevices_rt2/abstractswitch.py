from . import EcoDevicesRT2

from .const import (
    RESPONSE_ENTRY,
    RESPONSE_SUCCESS_VALUE,
)


class AbstractSwitch:
    """Class representing an AbstractSwitch"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int, get_link: str, get_entry: str, on_link: str, off_link: str, toggle_link: str) -> None:
        self._ecort2 = ecort2
        self._id = id
        self._get_link = get_link
        self._get_entry = get_entry
        self._on_link = on_link
        self._off_link = off_link
        self._toggle_link = toggle_link

    @property
    def status(self) -> bool:
        """Return the current AbstractSwitch status."""
        response = self._ecort2.get(self._get_link)
        return response[self._get_entry % (self._id)] == 1

    @status.setter
    def status(self, value: bool):
        if (value):
            self.on()
        else:
            self.off()

    def on(self) -> bool:
        """Turn on a the AbstractSwitch."""
        response = self._ecort2.get(self._on_link % (self._id))
        return response[RESPONSE_ENTRY] == RESPONSE_SUCCESS_VALUE

    def off(self) -> bool:
        """Turn off a AbstractSwitch."""
        response = self._ecort2.get(self._off_link % (self._id))
        return response[RESPONSE_ENTRY] == RESPONSE_SUCCESS_VALUE

    def toggle(self) -> bool:
        """Toggle a AbstractSwitch."""
        response = self._ecort2.get(self._toggle_link % (self._id))
        return response[RESPONSE_ENTRY] == RESPONSE_SUCCESS_VALUE
