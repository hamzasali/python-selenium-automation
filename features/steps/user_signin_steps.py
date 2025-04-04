from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.app.side_menu.click_sign_in_from_menu()


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()
