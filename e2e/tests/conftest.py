import pytest
from fixtures.setup import browser_context


@pytest.fixture
def page(browser_context):
    return browser_context
