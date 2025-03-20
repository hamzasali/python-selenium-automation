from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test=boxEmptyMsg]").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text
