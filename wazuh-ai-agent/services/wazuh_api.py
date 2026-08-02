import requests
import urllib3

from config import WAZUH_URL, WAZUH_USER, WAZUH_PASSWORD


urllib3.disable_warnings()


class WazuhAPI:

    def __init__(self):
        self.token = None


    def authenticate(self):
        response = requests.post(
            f"{WAZUH_URL}/security/user/authenticate",
            auth=(WAZUH_USER, WAZUH_PASSWORD),
            verify=False
        )

        response.raise_for_status()

        self.token = response.json()["data"]["token"]

        print("WAZUH TOKEN OK")

        return self.token


    def get_agents(self):

        if self.token is None:
            self.authenticate()


        headers = {
            "Authorization": f"Bearer {self.token}"
        }


        response = requests.get(
            f"{WAZUH_URL}/agents",
            headers=headers,
            verify=False
        )


        response.raise_for_status()

        return response.json()
