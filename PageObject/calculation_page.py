from playwright.sync_api import Page, expect


class CalculationPage:
    def __init__(self, page):
        self.page = page
        """Свитчер Скрыть столешницу"""
        self.hide_countertop_button = page.locator("//div[@data-testid='hide-countertop']")
        """Кнопка Показать столешницу"""
        self.show_countertop_button = page.locator("//div[@data-testid='show-main']")
        """Параметры отображения мойки"""
        self.washing_param = page.locator('div[data-testid="select-washing-countertop"]')
        """Кнопка П-образный тип столешницы"""
        self.countertop_p_example = page.locator("button[data-testid='countertop-type-u']")


    """Установить функции 'Скрыть столешницу' требуемое состояние"""
    def hide_countertop_set_state(self, active: bool):
        """Текущее состояние функции 'Скрыть столешницу'"""
        current_state = self.get_hide_countertop_state()
        if current_state:
            if active:
                return
            else:
                self.hide_countertop_button.click()


    """Получить текущее состояние кнопки 'Скрыть столешницу'"""
    def get_hide_countertop_state(self):
        """Состояние по умолчанию = включено"""
        state = True
        html_content = self.hide_countertop_button.locator("//img").get_attribute("src")
        if html_content and "/inactive" in html_content:
            state = False
            return state
        else:
            return state


    """Установить тип столешницы = П-Образная"""
    def set_countertop_on_t_example(self):
        self.countertop_p_example.click()