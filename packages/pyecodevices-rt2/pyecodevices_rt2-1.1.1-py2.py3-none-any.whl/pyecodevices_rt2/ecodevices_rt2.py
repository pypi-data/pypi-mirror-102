import requests

from .exceptions import (
    EcoDevicesRT2ConnectError,
    EcoDevicesRT2RequestError,
)

from .const import (
    PRODUCT_ENTRY,
    PRODUCT_VALUE,
    INDEX_GET_LINK,
    RESPONSE_ENTRY,
    RESPONSE_SUCCESS_VALUE,
)


class EcoDevicesRT2:
    """Class representing the Ecodevices RT2 and its API"""

    def __init__(self, host: str, port: int = 80, apikey: str = "", timeout: int = 10):
        self._host = host
        self._port = port
        self._apikey = apikey
        self._apiurl = "http://%s:%s/api/xdevices.json?key=%s" % (str(host), str(port), str(apikey))
        self._timeout = timeout

    @property
    def host(self):
        """Return the hostname."""
        return self._host

    @property
    def apikey(self):
        """Return the apikey."""
        return self._apikey

    @property
    def apiurl(self):
        """Return the default apiurl."""
        return self._apiurl

    def _request(self, params):
        r = requests.get(
            self._apiurl,
            params=params,
            timeout=self._timeout)
        r.raise_for_status()
        content = r.json()
        product = content.get(PRODUCT_ENTRY, None)
        if product == PRODUCT_VALUE:
            return content
        else:
            raise EcoDevicesRT2ConnectError("Ecodevices RT2 API wrong 'product' name\nUrl: %s \nValues: %s" % (r.request.url, content))

    def ping(self) -> bool:
        try:
            return self.get(INDEX_GET_LINK, command_entry=RESPONSE_ENTRY) == RESPONSE_SUCCESS_VALUE
        except:
            pass
        return False

    def get(self, command, command_value=None, command_entry=None):
        """Get value from api : http://{host}:{port}/api/xdevices.json?key={apikey}&{command}={command_value},
        then get value {command_entry} in JSON response."""
        complete_command = command
        if (command_value is not None):
            complete_command = command + "=" + command_value
        response = self._request(complete_command)
        if command_entry is not None:
            if command_entry in response:
                response = response.get(command_entry)
            else:
                raise EcoDevicesRT2RequestError(
                    "Ecodevices RT2 API error, key '%s' not in return from command: %s \nValues: %s"
                    % (command_entry, complete_command, response))
        return response
