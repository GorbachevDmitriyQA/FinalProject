from playwright.sync_api import Page, expect

"""Страница Калькулятор столешниц"""
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
        """Толщина столешницы"""
        self.top_thickness = page.locator("//label[contains(text(),'Толщина')]/parent::div[@data-testid='select-thickness']//button")
        """Опция Плинтус"""
        self.top_plintus_option = page.locator("//div[contains(text(),'Плинтус')]/parent::button")
        """Опция Остров"""
        self.island_option = page.locator("//h4[contains(text(),'Остров')]//ancestor::div[@data-testid='product-item']")
        """Опция Проточки для стакана воды"""
        self.grooves_of_water_option = page.locator("//h4[contains(text(),'Проточки для стока воды')]//ancestor::div[@data-testid='options-item']")


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

    """Получить цвет камня для столешницы по его имени/названию"""
    def get_stone_color_by_text(self, stone_name: str):
        return (self.page.locator
                (f"//div[@data-testid='stones']"
                 f"//div[@class='stoneName' and contains(text(),'{stone_name}')]"))

    """Установить толщину столешницы"""
    def set_top_thickness(self, thickness: str):
        current_value = self.top_thickness.text_content()
        if current_value == thickness:
            return
        else:
            self.top_thickness.click()
            self.top_thickness.locator(f"//span[contains(text(),'{thickness}')]").click()


    """Отключить опцию Плинтус"""
    def off_plintus_option(self):
        if self.top_plintus_option.locator("//img[@alt='ok-green']").count() == 0:
            return
        else:
            self.top_plintus_option.click()

    """Добавить опцию Остров"""
    def add_island_option(self):
        if self.island_option.locator("//img[@alt='ok-white']").count() == 1:
            return
        else:
            self.island_option.click()

    """Добавить опцию Проточки для стока воды"""
    def add_grooves_of_water_option(self):
        if self.grooves_of_water_option.locator("//img[@alt='ok-white']").count() == 1:
            return
        else:
            self.grooves_of_water_option.click()

    """Установить цвет камня столешницы"""
    def set_stone_color(self, stone_color: str):
        self.get_stone_color_by_text(stone_color).click()