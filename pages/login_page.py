from playwright.sync_api import Locator

from config.env_config import env_config
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self) -> None:
        super().__init__()

    @property
    def username_field(self) -> Locator:
        return self.page.locator('#login-form-username')

    @property
    def password_field(self) -> Locator:
        return self.page.locator('#login-form-password')

    @property
    def login_button(self) -> Locator:
        return self.page.locator('#login')

    def login(self) -> None:
        self.page.goto(self.url)
        self.username_field.fill(env_config.login.username)
        self.password_field.fill(env_config.login.password)
        self.login_button.click()

        self.driver.sleep(2)
