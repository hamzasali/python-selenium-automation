from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')
    sleep(3)
    result = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']").text
    expected = 'Sign into your Target account'
    assert expected in result
