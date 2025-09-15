import allure
from StepsManager.calculation_steps import CalculationSteps

@allure.title("Проверить работоспособности переключателя 'Скрыть столешницу'")
@allure.suite("UI Tests")
@allure.sub_suite("Calculation test")
def test_success_hide_countertop(page, user_auth):
    calc_steps = CalculationSteps(page)
    calc_steps.validations.check_countertop_is_displayed()
    (calc_steps.set_hide_countertop_to_inactive_state()
     .validations.check_hide_countertop_success())