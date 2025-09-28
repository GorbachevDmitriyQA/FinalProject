import allure
from StepsManager.calculation_steps import CalculationSteps
import pytest

@allure.title("Сквозной сценарий оформления заказа")
@pytest.mark.parametrize('order_data', ['test_e2e.json'], indirect=True)
def test_end_to_end(page, user_auth, order_data):
    steps = CalculationSteps(page)
    steps.create_order(order_data)
    steps.calculate_order()
    steps.calculate_info_click(order_data)
    steps.validations.check_calculation_result_page_is_loaded()
    steps.validations.check_calc_results_order_param(order_data)