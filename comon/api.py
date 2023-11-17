import json
import requests
from urllib.parse import urljoin
from .models import Status
from .utils import snake_to_camel, remove_none_values


class Client:
    def __init__(self, base_url, verify_ssl=True):
        self.base_url = base_url
        self.verify_ssl = verify_ssl

    def create_status(self, package_guid: str, status: Status) -> dict:
        """
        Create a status for a given package GUID.

        :param package_guid: The GUID of the package.
        :param status: An instance of the Status class.
        :return: A dictionary containing the response data.
        """
        url = urljoin(self.base_url, "/api/services/app/External/CreateStatus")
        url_params = {"packageGuid": package_guid}

        response = requests.post(
            url,
            verify=self.verify_ssl,
            json=remove_none_values(snake_to_camel(status.json())),
            params=url_params,
        )

        if (
            response.status_code != 200
            or "application/json" not in response.headers.get("Content-Type", "")
        ):
            raise ValueError(
                "Failed to create status. Status code: {}".format(response.status_code)
            )

        try:
            return response.json()
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse response JSON. Error: {e}")
