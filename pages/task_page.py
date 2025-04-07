from playwright.sync_api import Locator

from pages.base_page import BasePage
from config.env_config import env_config


class TaskPage(BasePage):
    def __init__(self) -> None:
        super().__init__()
        self.url = self.compose_url(env_config.task.reference_task)

    def open(self) -> None:
        self.page.goto(self.url)

    @property
    def more_dropdown(self) -> Locator:
        return self.page.locator('#opsbar-operations_more')

    @property
    def clone_dropdown_item(self) -> Locator:
        return self.page.locator('//aui-item-link[contains(., "Clone")]')

    @property
    def summary_field(self) -> Locator:
        return self.page.locator('#summary')

    @property
    def create_button(self) -> Locator:
        return self.page.locator('#clone-issue-submit')


    @property
    def description_content_block(self) -> Locator:
        return self.page.locator('.user-content-block')

    @property
    def description_field(self) -> Locator:
        return self.page.locator('#description')

    @property
    def save_button(self) -> Locator:
        return self.page.locator('.submit')

    @property
    def clone_issue_content(self) -> Locator:
        return self.page.locator('//div[@class="link-content"]')

    @property
    def clone_issue_delete_link(self) -> Locator:
        return self.page.locator('//div[@class="delete-link"]/a')

    @property
    def issue_link_delete_button(self) -> Locator:
        return self.page.locator('#issue-link-delete-submit')