import pytest
import allure
from playwright.sync_api import Page
from PageObject.header_page_block import HeaderBlockPage
from StepsManager.Validations.base_steps_validations import BaseStepsValidations
from Tests.config import *

class BaseSteps:
    def __init__(self, page: Page):
        self.page = page
        """Проверки для текущего класса"""
        self.validations = BaseStepsValidations(self.page)
        """Страница с элементами header системы"""
        self.header_block_page = HeaderBlockPage(page)

    """Выполнить авторизацию в системе"""
    def login(self, username=base_username, password=base_password):
        with allure.step(f"Выполнить авторизацию в системе"
                         f" username: {username}, password: {password}"):
            self.header_block_page.login(username, password)
        return self