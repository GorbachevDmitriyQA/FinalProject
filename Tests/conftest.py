import os.path
from multiprocessing import context

import pytest
from playwright.sync_api import sync_playwright
import  screeninfo
from playwright.sync_api import expect
expect.set_options(timeout=12340)
from Tests.config import *
from StepsManager.base_steps import BaseSteps
import json
from DataModels.order_data import OrderData
from pathlib import Path

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Получим размеры экрана
        try:
            from screeninfo import get_monitors
            monitor = get_monitors()[1]
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

"""Выполнить вход в систему"""
@pytest.fixture
def user_auth(page):
    steps = BaseSteps(page)
    steps.login()

@pytest.fixture
def order_data(request):
    json_str = get_json_file_as_string(request.param)
    data = json.loads(json_str)
    obj = OrderData(**data)
    return obj

"""Получение тест даты"""
def get_json_file_as_string(filename):
    this_dir = Path(__file__).parent
    # На уровень выше и в TestData
    testdata_dir = (this_dir.parent / 'TestData').resolve()
    final_path = os.path.join(testdata_dir, filename)
    with open(final_path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data


def switch_to_last_page(page):
    pages = context.pages
    print(f"Открытые вкладки: {pages}")

    # Получаем последнюю вкладку:
    last_page = pages[-1]
    print(f"Последняя вкладка: {last_page}")

    # Дальше работаем с last_page
    last_page.bring_to_front()