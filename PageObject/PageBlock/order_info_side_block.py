from playwright.sync_api import Page, expect
"""Блок с информацией о заказе"""
class OrderInfoSideBlock:
    def __init__(self, page):
        self.page = page
        self.context = page.context
        """Кнопка рассчитать"""
        self.calculate_buton = page.locator("button[data-testid='calc-button']")

        """Нажать кнопку Рассчитать"""
    def calculate_info_button_click(self):
        self.calculate_buton.click()