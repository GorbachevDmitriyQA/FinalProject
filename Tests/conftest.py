import allure
import pytest
from playwright.sync_api import sync_playwright
import  screeninfo
from playwright.sync_api import expect
expect.set_options(timeout=12340)
from Tests.config import *

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Получим размеры экрана
        try:
            from screeninfo import get_monitors
            monitor = get_monitors()[0]
            width, height = monitor.width, monitor.height
        except ImportError:
            width, height = 1920, 1080

        browser = p.chromium.launch(headless=False,
                                    )
        context = browser.new_context(
            viewport={'width': width, 'height': height},
        ignore_https_errors=True)
        page = context.new_page()
        page.goto(base_url)
        yield page
        browser.close()