import allure
from StepsManager.base_steps import BaseSteps


@allure.title("Успешная авторизация")
@allure.suite("UI Tests")
@allure.sub_suite("Auth Tets")
def test_auth_success(page):
    base_steps = BaseSteps(page)
    (base_steps.login()
     .validations.success_auth_validate(expected_name="Tester"))
