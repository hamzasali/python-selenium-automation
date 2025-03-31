from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    context.driver.wait.until(EC.text_to_be_present_in_element(
        ((By.CSS_SELECTOR, "[class*='styles_ndsHeading']")), 'Sign into your Target account')
    )


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')
    result = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']").text
    expected = 'Sign into your Target account'
    assert expected in result, f'expected: {expected}, but got {result}'
