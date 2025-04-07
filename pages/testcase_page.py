from pages.base_page import BasePage
from playwright.sync_api import Locator


class TestcasePage(BasePage):
    def __init__(self) -> None:
        super().__init__()

    def open(self, sir_number: str = '') -> None:
        self.page.goto(self.compose_url(sir_number))

    @property
    def task_title(self) -> Locator:
        return self.page.locator('#summary-val')

    @property
    def task_url(self) -> str:
        return self.page.url

    @property
    def collected_test_case_data(self) -> dict:
        return {
            'Title': self.task_title.text_content(),
            'URL': self.task_url,
        }