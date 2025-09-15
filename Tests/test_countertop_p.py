import allure
from StepsManager.calculation_steps import CalculationSteps


@allure.title("Переключение на П-образную столешницу")
@allure.suite("UI Tests")
@allure.sub_suite("Calculation test")
def test_success_change_countertop_p(page, user_auth):
    steps = CalculationSteps(page)
    (steps.set_countertop_on_t_example()
     .validations.check_countertop_p_example_success())