from pages.login_page import LoginPage
from pages.testcase_page import TestcasePage
from pages.task_page import TaskPage
import platform

TESTCASE_TITLE: str = 'Cover "{0}"'
TESTCASE_TO_CREATE: list[str] = ['']


class StartCreatingTasks:
    def __init__(self) -> None:
        self.login_page = LoginPage()
        self.testcase_page = TestcasePage()
        self.task_page = TaskPage()

    def start(self):
        # login
        self.login_page.login()
        # Main cycle to creating tasks
        for testcase_number in TESTCASE_TO_CREATE:
            # Get data from the testcase
            self.testcase_page.open(testcase_number)
            testcase_data = self.testcase_page.collected_test_case_data

            # Create a new task
            self.task_page.open()

            # Clone the task
            self.task_page.more_dropdown.click()
            self.task_page.clone_dropdown_item.click()
            self.task_page.summary_field.fill(
                TESTCASE_TITLE.format(testcase_data.get("Title")))
            self.task_page.create_button.click()

            # Add link to the description

            self.task_page.description_content_block.click()
            self.task_page.description_field.press(
                f'{"Meta" if platform.system() == "Darwin" else "Control"}+A')
            self.task_page.description_field.fill(testcase_data.get('URL'))
            self.task_page.save_button.click()

            # Delete the "cloned by" task from
            self.task_page.clone_issue_content.hover()
            self.task_page.clone_issue_delete_link.click()
            self.task_page.issue_link_delete_button.click()

            print(f'Last testcase: {testcase_data.get("URL")}')
            print(f'Last created task: {self.task_page.page.url}')
            print('*' * 60)


if __name__ == '__main__':
    create_task = StartCreatingTasks()
    create_task.start()
