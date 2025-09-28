from playwright.sync_api import Page, expect, BrowserContext
from PageObject.page_base import PageBase

"""Страница Обработчики"""
class HandlersPage(PageBase):

    def __init__(self, page):
        self.page = page
        self.context = self.page.context
        """Кнопка Расчет"""
        self.calculation_info_button = page.locator("button[data-testid='open-report-button']")
        """Итоговая сумма заказа"""
        self.sum_price = page.locator("//*[@data-testid='price-button']")

    """Нажать кнопку расчет (с переключением на новую вкладку)"""
    def calculate_info_button_click(self, switch_to_new_tab=True):
        with self.context.expect_page() as new_tab:
            self.calculation_info_button.click()
            new_tab = new_tab.value
            # if switch_to_new_tab:
            #     new_tab.bring_to_front()
            return new_tab
