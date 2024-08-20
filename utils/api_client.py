import requests
from config.config import BASE_URL


class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        """Send a GET request to the API"""
        response = None
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad status code
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return response

    def post(self, endpoint, data=None):
        """Send a POST request to the API"""
        response = None
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()  # Raise and error for bad status code
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return response

    def put(self, endpoint, data=None):
        """Send a PUT request to the API"""
        response = None
        try:
            response = requests.put(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return response

    def delete(self, endpoint):
        """Send a DELETE request to the API"""
        response = None
        try:
            response = requests.delete(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        return response
