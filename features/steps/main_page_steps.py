from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[id*=utilityNav]")


@given('Open target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(12)


@when('Click on cart')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    context.driver.wait.until(EC.url_matches('https://www.target.com/cart'))


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()
    context.driver.wait.until(EC.element_to_be_clickable(((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))))


@then('Verify at least 1 links shown')
def verify_header_link_shown(context):
    links = context.driver.find_element(*HEADER_LINKS)
    print(links)


@then('Verify {link_amount} links are shown')
def verify_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == link_amount, f'Expected {link_amount} links but got {len(links)}'
