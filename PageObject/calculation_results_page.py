from asyncio import wait_for

from playwright.sync_api import Page, expect

"""Страница Результаты расчета"""
class CalculationResultsPage:
    def __init__(self, page):
        self.page = page
        """Материал - значение"""
        self.material_value = self.page.locator("//td[contains(text(),'Материал')]/following-sibling::td[1]")
        """Тип столешницы"""
        self.top_type_value = self.page.locator("//td[contains(text(),'Тип столешницы')]/following-sibling::td[1]")
        """Опции"""
        self.option_value = self.page.locator("//td[contains(text(),'Опции')]/following-sibling::td[1]")
        """Стоимость итоговая"""
        self.sum_price = self.page.locator("//td[contains(text(),'Стоимость итоговая')]/following-sibling::td[3]")

    """Получить текст заголовка страницы"""
    def get_header_page_text(self):
        return self.page.locator("//h1").inner_text()


    def get_material_value_text(self):
        return self.material_value.inner_text()
