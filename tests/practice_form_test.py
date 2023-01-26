import allure
from allure_commons.types import Severity

from demoqa_tests.model.pages.practice_form import Form
from demoqa_tests.data.user_data import nikita


@allure.title("Successful fill form")
def test_submitting_form():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'nikita')
    allure.dynamic.feature('Successful fill form')

    form = Form()

    with allure.step('заполнение формы'):
        form.submit_form(nikita)

    with allure.step('проверка формы'):
        form.validate_form(nikita)
