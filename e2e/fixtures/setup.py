import pytest
from playwright.sync_api import sync_playwright


class PlaywrightManager:
    def __init__(
        self,
        headless: bool = False,  # Set to False to avoid "not secure" error
        trace_path: str = "trace.zip",
        user_data_dir: str = "/tmp/playwright",  # Persistent context directory
    ):
        self.headless = headless
        self.trace_path = trace_path
        self.user_data_dir = user_data_dir
        self.browser = None
        self.context = None

    def __enter__(self):
        self.playwright = sync_playwright().start()

        # Launch with automation-controlled flag disabled
        self.browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            headless=self.headless,
            args=["--disable-blink-features=AutomationControlled"],
            viewport={"width": 1280, "height": 720},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            color_scheme="dark",
        )

        self.context = self.browser
        self.context.set_default_timeout(60000)

        # Grant permissions for clipboard, microphone, etc.
        self.context.grant_permissions(
            permissions=["microphone", "clipboard-read", "clipboard-write"]
        )

        # Start tracing
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        return self.context.pages[0] if self.context.pages else self.context.new_page()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context.tracing.stop(path=self.trace_path)
        self.context.close()
        self.playwright.stop()


@pytest.fixture(scope="function", autouse=True)
def browser_context():
    """Pytest fixture to provide a browser page context."""
    with PlaywrightManager() as page:
        yield page
