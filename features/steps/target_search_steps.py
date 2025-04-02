from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    context.driver.wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "[class*='styles_ndsHeading']"), 'Sign into your Target account')
    )


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    # context.driver.execute_script("window.scrollBy(0,2000)", "")
    # sleep(2)
    # context.driver.execute_script("window.scrollBy(0,1000)", "")
    # sleep(2)

    products = context.driver.find_elements(*LISTINGS)[:8]  # [WebEl1, WebEl2, WebEl3, WebEl4]

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')
    result = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']").text
    expected = 'Sign into your Target account'
    assert expected in result, f'expected: {expected}, but got {result}'
