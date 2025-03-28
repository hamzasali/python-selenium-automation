from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*=addToCartButton]")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper']  [id*=addToCart]")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@then('Verify correct search result shown for {expected_text}')
def verify_search_result(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@when('Click add to cart btn')
def click_add_to_cart(context):
    context.driver.execute_script("window.scrollTo(0, 1200);")
    sleep(3)
    # context.driver.find_elements(*ADD_TO_CART_BTN)[2].click()
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(4)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()
    sleep(5)


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print("Product name stored: ", context.product_name)
