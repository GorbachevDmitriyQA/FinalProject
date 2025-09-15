import pytest
from playwright.sync_api import Page
from Tests.config import *

"""Блок с шапкой сервиса Topklik.online"""


class HeaderBlockPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_field = page.locator("input[name='login']")
        self.password_field = page.locator("input[name='pass']")
        self.login_button = page.locator("//button[contains(text(),'Войти')]")
        self.logout_button = page.locator("//button[contains(text(),'Выйти')]")
        self.user_name = page.locator(".style_loginBar__ozcMd h2")


    """Выполнить вход в систему"""
    def login(self, username: str, password: str):
        self.login_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()


    """Получить имя авторизованного пользователя в header"""
    def get_authorized_user_name(self):
        return self.user_name.text_content()
