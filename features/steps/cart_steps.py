from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test=boxEmptyMsg]")
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@when('Open Cart')
def open_cart(context):
    context.driver.get("https://www.target.com/cart")


@then('Verify Cart has {quantity} item')
def verify_cart_has_one_item(context, quantity):
    context.driver.find_element(*CART_SUMMARY)


@then('Verify cart has correct product')
def verify_product(context):
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Name in Cart: ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected: {context.product_name[:20]} did not match {product_name_in_cart[:20]}'
