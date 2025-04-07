from playwright.async_api import Page
from config.driver import Driver


class BasePage:
    def __init__(self) -> None:
        self.driver = Driver.get_instance()
        self.page: Page = self.driver.page
        self.url = 'https://jira.com'

    def compose_url(self, path) -> str:
        return f'{self.url}/browse/{path}'
