import pytest
from playwright.sync_api import expect, Page
import re
import os
import allure
from PageObject.header_page_block import HeaderBlockPage
from StepsManager.base_steps import BaseSteps


@allure.title("Успешная авторизация")
@allure.suite("UI Tests")
@allure.sub_suite("Auth Tets")
def test_auth_success(page):
    base_steps = BaseSteps(page)
    (base_steps.login()
     .validations.success_auth_validate(expected_name="Tester"))
