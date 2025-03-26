from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")


@then('Verify correct search result shown for {expected_text}')
def verify_search_result(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@when('Click add to cart btn')
def click_add_to_cart(context):
    context.driver.execute_script("window.scrollTo(0, 1000);")
    context.driver.find_elements(By.CSS_SELECTOR, "[id*=addToCartButton]")[2].click()
    # context.driver.find_elements(By.XPATH, "//button[@id=contains(text(), 'addToCartButtonOrTextId')]")[2].click()
    sleep(6)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='content-wrapper'] button[data-test='orderPickupButton'][id*=addToCart]").click()
    sleep(5)
