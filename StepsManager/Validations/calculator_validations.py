import allure
from pyexpat.errors import messages

from PageObject.calculation_page import CalculationPage
from playwright.sync_api import Page, expect
from DataModels.order_data import OrderData
from PageObject.calculation_results_page import CalculationResultsPage
from PageObject.page_base import PageBase


class CalculatorValidations(PageBase):
    def __init__(self, page: Page):
        super().__init__(page)
        self.calculation_result = None
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

    """Проверить успешность открытия страницы Результаты расчета"""
    def check_calculation_result_page_is_loaded(self):
        with allure.step("Проверить, что открылась страница с результатами расчета"):
            self.calculation_result = CalculationResultsPage(super().get_the_last_tab())
            header_text = self.calculation_result.get_header_page_text()
            assert header_text == "Результаты расчета"

    """Проверить параметры расчета"""
    def check_calc_results_order_param(self, data: OrderData):
        with allure.step(f"Проверить, что значение Материал = {data.top_color}"):
            color = self.calculation_result.get_material_value_text()
            assert data.top_color in color, f"Материал не совпадает с ожидаемым: {color}"
        with allure.step("Проверить тип столешницы"):
            if data.p_example_option:
                expect(self.calculation_result.top_type_value,
                       message="Тип столешницы П-Образная не найден").to_have_text("П-образная")
        with allure.step("Проверить опции"):
            if data.grooves_of_water_option:
                expect(self.calculation_result.option_value,
                       message="Опция Проточки для стока воды не найдена").to_have_text("Проточки для стока воды")
        with allure.step("Проверить итоговую стоимость"):
            expect(self.calculation_result.sum_price,
                   message="Итоговая стоимость не совпадает с ожидаемой").to_have_text(data.sum_price)
