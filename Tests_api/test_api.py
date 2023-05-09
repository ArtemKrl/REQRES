import pytest


class TestAPI:

    @pytest.mark.parametrize("user_id", [1, 2])
    def test_get_single_user(self, user_api, user_id):
        response = user_api.get_single_user(user_id)
        assert response.status_code == 200
        assert "data" in response.json()
        assert response.json()["data"]["id"] == user_id

    @pytest.mark.parametrize("user_id", [999, 777])
    def test_get_single_user_not_found(self, user_api, user_id):
        response = user_api.get_single_user(user_id)
        assert response.status_code == 404
        assert response.json() == {}

    @pytest.mark.parametrize("name , job", [("Boris Britwa", "Arms Dealer"),
                                            ("Billy Harringhthon", "Full master")])
    def test_post_create_user(self, user_api, name, job):
        payload = {
            "name": name,
            "job": job
        }
        response = user_api.create_user(payload)
        assert response.status_code == 201
        assert "id" in response.json()
        assert response.json()["name"] == name
        assert response.json()["job"] == job
