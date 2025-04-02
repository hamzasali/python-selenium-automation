from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*=addToCartButton]")
ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper']  [id*=addToCart]")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@then('Verify correct search result shown for {expected_text}')
def verify_search_result(context, expected_text):
    context.app.search_result_page.verify_search_result(expected_text)


@when('Click add to cart btn')
def click_add_to_cart(context):
    # context.driver.execute_script("window.scrollTo(0, 1200);")
    # context.driver.find_elements(*ADD_TO_CART_BTN)[2].click()
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN_SIDE_NAV))


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN_SIDE_NAV).click()


@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
                              message='product name not visible')
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print("Product name stored: ", context.product_name)
