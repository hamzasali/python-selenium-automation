from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

import app

HEADER_LINKS = (By.CSS_SELECTOR, "[id*=utilityNav]")


@given('Open target main page')
def open_target_page(context):
    context.app.main_page.open_main_page()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)
    sleep(12)


@when('Click on cart')
def click_cart(context):
    context.app.header.click_cart()
    context.driver.wait.until(EC.url_matches('https://www.target.com/cart'))


@when('Click Sign in')
def click_sign_in(context):
    context.app.header.click_sign_in()
    # context.driver.wait.until(EC.element_to_be_clickable(((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))))


@then('Verify at least 1 links shown')
def verify_header_link_shown(context):
    links = context.driver.find_element(*HEADER_LINKS)
    print(links)
    # Stale Element Reference Ex
    # print("Before refresh:", link)
    # context.driver.refresh()
    # link = context.driver.find_element(*HEADER_LINKS)
    # link.click()
    # print("AFTER refresh:", link)


@then('Verify {link_amount} links are shown')
def verify_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    assert len(links) == link_amount, f'Expected {link_amount} links but got {len(links)}'
