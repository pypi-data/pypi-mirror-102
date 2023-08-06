from . import EcoDevicesRT2, AbstractSwitch

from .const import (
    RELAY_GET_LINK,
    RELAY_GET_ENTRY,
    RELAY_ON_LINK,
    RELAY_OFF_LINK,
    RELAY_TOGGLE_LINK,
)


class Relay(AbstractSwitch):
    """Class representing the Relay"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int) -> None:
        super(Relay, self).__init__(
            ecort2, id,
            RELAY_GET_LINK, RELAY_GET_ENTRY,
            RELAY_ON_LINK, RELAY_OFF_LINK, RELAY_TOGGLE_LINK)
