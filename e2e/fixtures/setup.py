import pytest
from playwright.sync_api import sync_playwright


class PlaywrightManager:
    def __init__(
        self,
        headless: bool = True,
        no_viewport: bool = True,
        trace_path: str = "trace.zip",
    ):
        self.headless = headless
        self.no_viewport = no_viewport
        self.trace_path = trace_path
        self.browser = None
        self.context = None

    def __enter__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(
            no_viewport=self.no_viewport, color_scheme="dark"
        )
        self.context.grant_permissions(
            permissions=["microphone", "clipboard-read", "clipboard-write"]
        )
        self.context.set_default_timeout(60000)
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        return self.context.new_page()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context.tracing.stop(path=self.trace_path)
        self.context.close()
        self.browser.close()
        self.playwright.stop()


@pytest.fixture(scope="function", autouse=True)
def browser_context():
    """Returns a browser context."""
    with PlaywrightManager() as page:
        yield page
