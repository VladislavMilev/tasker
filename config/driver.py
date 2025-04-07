from playwright.sync_api import Page, sync_playwright


class Driver:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(
                headless=False,
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--enable-automation',
                    '--disable-features=IsolateOrigins,site-per-process',
                    '--flag-switches-begin --disable-site-isolation-trials',
                    '--flag-switches-end',
                    '--no-sandbox',
                    '--start-maximized',
                ],
            )
            self.context = self.browser.new_context(no_viewport=True)
            self.page: Page = self.context.new_page()

    @classmethod
    def get_instance(cls):
        return cls()

    def close(self):
        if hasattr(self, 'context') and self.context:
            self.context.close()
        if hasattr(self, 'browser') and self.browser:
            self.browser.close()
        if hasattr(self, 'playwright') and self.playwright:
            self.playwright.stop()

    def sleep(self, timeout: float) -> None:
        self.page.wait_for_timeout(timeout * 1000)
