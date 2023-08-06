from . import EcoDevicesRT2, AbstractSwitch

from .const import (
    VIRTUAL_OUTPUT_GET_LINK,
    VIRTUAL_OUTPUT_GET_ENTRY,
    VIRTUAL_OUTPUT_ON_LINK,
    VIRTUAL_OUTPUT_OFF_LINK,
    VIRTUAL_OUTPUT_TOGGLE_LINK,
)


class VirtualOutput(AbstractSwitch):
    """Class representing the VirtualOutput"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int) -> None:
        super(VirtualOutput, self).__init__(
            ecort2, id,
            VIRTUAL_OUTPUT_GET_LINK, VIRTUAL_OUTPUT_GET_ENTRY,
            VIRTUAL_OUTPUT_ON_LINK, VIRTUAL_OUTPUT_OFF_LINK, VIRTUAL_OUTPUT_TOGGLE_LINK)
