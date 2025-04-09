from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TERM_CONDITIONS_BTN = (By.CSS_SELECTOR, "[data-test='@web/component-footer/LegalLink'][href*='terms-conditions']")


@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.app.side_menu.click_sign_in_from_menu()


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.wait_until_clickable_click(*TERM_CONDITIONS_BTN)


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.sign_in_page.verify_partial_url('terms-conditions')
