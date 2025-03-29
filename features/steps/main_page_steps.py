from selenium.webdriver.common.by import By
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
    sleep(10)


@when('Click on cart')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(3)


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '#account-sign-in').click()
    sleep(3)


@then('Verify at least 1 links shown')
def verify_header_link_shown(context):
    sleep(3)
    links = context.driver.find_element(*HEADER_LINKS)
    print(links)


@then('Verify {link_amount} links are shown')
def verify_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    sleep(3)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == link_amount, f'Expected {link_amount} links but got {len(links)}'
