from playwright.sync_api import Page
from PageObject.calculation_page import CalculationPage
from StepsManager.Validations.calculator_validations import CalculatorValidations
import allure

"""Шаги по работе с калькулятором"""
class CalculationSteps:
    def __init__(self, page: Page):
        self.page = page
        self.calculation_page = CalculationPage(self.page)
        self.validations = CalculatorValidations(self.page)

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