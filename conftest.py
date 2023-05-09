import pytest
from api_config.user_api import UserAPI
from selenium import webdriver


@pytest.fixture(scope="module")
def user_api():
    base_url = "https://reqres.in"
    return UserAPI(base_url)


@pytest.fixture(scope="module")
def browser():
    # Инициализация экземпляра браузера перед выполнением всех тестов
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после выполнения всех тестов
    driver.quit()
