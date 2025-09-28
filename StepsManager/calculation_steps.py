from playwright.sync_api import Page

from PageObject.PageBlock.order_info_side_block import OrderInfoSideBlock
from PageObject.calculation_page import CalculationPage
from PageObject.calculation_results_page import CalculationResultsPage
from PageObject.handlers_page import HandlersPage
from PageObject.page_base import PageBase
from StepsManager.Validations.calculator_validations import CalculatorValidations
import allure
from DataModels.order_data import OrderData

"""Шаги по работе с калькулятором"""
class CalculationSteps(PageBase):
    def __init__(self, page: Page):
        super().__init__(page)
        self.calculation_results = None
        self.page = page
        self.calculation_page = CalculationPage(self.page)
        self.validations = CalculatorValidations(self.page)
        self.order_info_side_block = OrderInfoSideBlock(self.page)
        self.handlers_page = HandlersPage(self.page)

    """Деактивировать функцию Скрыть столешницу"""
    def set_hide_countertop_to_inactive_state(self):
        with allure.step("Деактивировать функцию Скрыть столешницу"):
            self.calculation_page.hide_countertop_set_state(active=False)
        return self

    """Переключить тип столешницы на П-образную"""
    def set_countertop_on_t_example(self):
        with allure.step("Переключить тип столешницы на П-образную"):
            self.calculation_page.set_countertop_on_t_example()

        return self

    """Собрать заказ с параметрами"""
    def create_order(self, data: OrderData):
        with allure.step("Активировать опцию П-образная столешница"):
            if data.p_example_option:
                self.calculation_page.set_countertop_on_t_example()
        with allure.step(f"Установить толщину столешницы = {data.top_thickness}"):
            self.calculation_page.set_top_thickness(thickness=data.top_thickness)
        with allure.step(f"Опцию плинтус перевести в положение {data.plintus_option}"):
            if not data.plintus_option:
                self.calculation_page.off_plintus_option()
        with allure.step(f"Опцию Остров перевести в положение {data.island_option}"):
            if data.island_option:
                self.calculation_page.add_island_option()
        with allure.step(f"Опцию Проточки для стока воды перевести в положение {data.grooves_of_water_option}"):
            if data.grooves_of_water_option:
                self.calculation_page.add_grooves_of_water_option()
        with allure.step(f"Установить цвет столешницы {data.top_color}"):
            self.calculation_page.set_stone_color(data.top_color)

    """Нажать кнопку Рассчитать(заказ)"""
    def calculate_order(self):
        with allure.step("Нажать кнопку 'Рассчитать' заказ"):
            self.order_info_side_block.calculate_info_button_click()

    """Нажать кнопку Расчет на странице обработчики"""
    def calculate_info_click(self, data: OrderData):
        with allure.step("Запомнить итоговую сумму заказа"):
            sum = self.handlers_page.sum_price.inner_text()
            # 1. Удалить пробелы и неразрывные пробелы
            numeric = sum.replace('\xa0', '').replace(' ', '').replace('₽', '').strip()
            # 2. Преобразовать в число с плавающей точкой
            number = float(numeric)
            # 3. Сформировать строку с нужным форматом
            result = f"{number:.2f} ₽"
            data.sum_price = result
        with allure.step("Нажать кнопку 'Расчет'"):
            new_tab = self.handlers_page.calculate_info_button_click()
            self.calculation_results = CalculationResultsPage(new_tab)
