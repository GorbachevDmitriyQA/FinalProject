import allure

from PageObject.calculation_page import CalculationPage
from playwright.sync_api import Page, expect


class CalculatorValidations:
    def __init__(self, page: Page):
        self.page = page
        self.calculation_page = CalculationPage(self.page)


    """Проверить, что столешница не отображается при выкл 'Показать столешницу'"""
    def check_hide_countertop_success(self):
        with allure.step("Проверить, что столешница не отображается при выкл 'Показать столешницу'"):
            expect(self.calculation_page.show_countertop_button,
                   message="Кнопка показать столешницу не отображается").not_to_be_empty()
            assert self.calculation_page.washing_param.count()==0, ("Видимость элемента с "
                                                                 "параметром мойки не ожидалась")



    """Проверить, что столешница отображается при"
                         "вкл 'Показать столешницу'"""
    def check_countertop_is_displayed(self):
        with (allure.step("Проверить, что столешница отображается при"
                         "вкл 'Показать столешницу'")):
            assert self.calculation_page.get_hide_countertop_state() == True, \
                "Текущее состояние функции Скрыть столешницу не активно по умолчанию"
            expect(self.calculation_page.washing_param).to_be_visible()


    """Проверить что отображается П-образный тип столешницы"""
    def check_countertop_p_example_success(self):
        with (allure.step("Проверить что отображается П-образный тип столешницы")):
            expect(self.calculation_page.countertop_p_example
                   ).to_contain_class("style_active__+m9Cn")