import json
from web_config.HeadPage import HeadPage
from web_config.API_client import APIClient


class TestHeadPage:

    def test_ListUser_button(self, browser):
        head_page = HeadPage(browser)
        head_page.open()
        head_page.click_listuser_request_button()

        api_client = APIClient()
        expected_body, expected_status_code = api_client.get_listuser_response()

        response_text = head_page.get_response_text()
        response_status_code = head_page.get_response_status_code()

        # Проверка соответствия результатов
        assert response_text == json.dumps(expected_body, indent=4)
        assert int(response_status_code) == expected_status_code

    def test_Create_button(self, browser):
        head_page = HeadPage(browser)
        head_page.open()
        head_page.click_create_request_button()

        api_client = APIClient()
        expected_body, expected_status_code = api_client.get_create_response()

        response_text = head_page.get_response_text()
        response_status_code = head_page.get_response_status_code()

        assert response_text == json.dumps(expected_body, indent=4)
        assert int(response_status_code) == expected_status_code
