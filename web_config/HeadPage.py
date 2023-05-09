from selenium.webdriver.common.by import By


class HeadPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://reqres.in/")

    def click_listuser_request_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "li:nth-child(1) > a")
        button.click()

    def click_create_request_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "li:nth-child(7) > a")
        button.click()

    def get_response_text(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".response > pre").text

    def get_response_status_code(self):
        return self.browser.find_element(By.CSS_SELECTOR, "strong > span").text
