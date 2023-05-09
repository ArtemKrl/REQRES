import requests

class APIClient:

    def get_listuser_response(self):
        api_response = requests.get("https://reqres.in/api/users?page=2")
        return api_response.json(), api_response.status_code

    def get_create_response(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }

        api_response = requests.post("https://reqres.in/api/users", json=payload)
        return api_response.json(), api_response.status_code

