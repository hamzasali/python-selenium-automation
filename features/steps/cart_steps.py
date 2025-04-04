from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Verify cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@when('Open Cart')
def open_cart(context):
    context.app.cart_page.open_cart()


@then('Verify Cart has {quantity} item')
def verify_cart_has_one_item(context, quantity):
    context.app.cart_page.verify_cart_has_items()


@then('Verify cart has correct product')
def verify_product(context):
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print(f'Name in Cart: ', product_name_in_cart)
    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected: {context.product_name[:20]} did not match {product_name_in_cart[:20]}'

@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()
