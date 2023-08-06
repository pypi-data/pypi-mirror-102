from . import EcoDevicesRT2


class AbstractSensor:
    """Class representing an AbstractSensor"""

    def __init__(self, ecort2: EcoDevicesRT2, id: int, get_link: str, get_entry: str) -> None:
        self._ecort2 = ecort2
        self._id = id
        self._get_link = get_link
        self._get_entry = get_entry

    @property
    def value(self) -> float:
        """Return the current AbstractSensor status."""
        response = self._ecort2.get(self._get_link)
        return response[self._get_entry % (self._id)]
