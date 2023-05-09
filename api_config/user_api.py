import requests

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_single_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        response = requests.get(url)
        return response

    def create_user(self, user_data):
        url = f"{self.base_url}/api/users"
        response = requests.post(url, json=user_data)
        return response