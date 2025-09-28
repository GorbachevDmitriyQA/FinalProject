from playwright.sync_api import Page, expect, BrowserContext

"""Базовый класс всех страниц"""
class PageBase:
    def __init__(self, page: Page):
        self.page = page

    def switch_to_tab(self, index: int) -> None:
        """Переключение на вкладку по индексу"""
        self.page.wait_for_timeout(1000)  # Небольшая задержка для стабильности
        all_tabs = self.page.context.pages
        if index < len(all_tabs):
            self.page = all_tabs[index]
            self.page.bring_to_front()
        else:
            raise Exception(f"Вкладка с индексом {index} не существует")


    def get_the_last_tab(self):
        return self.page.context.pages[-1]