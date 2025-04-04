from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


@then('Verify correct search result shown for {expected_text}')
def verify_search_result(context, expected_text):
    context.app.search_results_page.verify_search_result(expected_text)


@then('Verify {expected_text} in URL')
def verify_results_url(context, expected_text):
    context.app.search_results_page.verify_results_url(expected_text)


@when('Click add to cart btn')
def click_add_to_cart(context):
    # context.driver.execute_script("window.scrollTo(0, 1200);")
    context.app.search_results_page.click_add_to_cart()


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.side_menu.click_add_to_cart_from_menu()

@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
                              message='product name not visible')
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print("Product name stored: ", context.product_name)
