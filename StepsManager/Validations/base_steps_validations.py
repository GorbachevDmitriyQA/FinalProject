import logging

from playwright.sync_api import Page, expect
from PageObject.header_page_block import HeaderBlockPage
import allure

"""Класс проверок для базовых шагов (BaseSteps)"""
class BaseStepsValidations:
    def __init__(self, page: Page):
        self.page = page
        """Страница с элементами header системы"""
        self.header_block_page = HeaderBlockPage(page)

    """Проверить успешную авторизацию в системе"""
    def success_auth_validate(self, expected_name: str):
        with allure.step(f"Проверить, что имя в header = {expected_name}"):
            current_name = self.header_block_page.get_authorized_user_name()
            allure.attach(
                f"Ожидаемое имя пользователя: {expected_name}\n"
                f"Текущее имя: {current_name}",
                name="Данные проверок",
                attachment_type=allure.attachment_type.TEXT
            )
            assert expected_name == current_name
