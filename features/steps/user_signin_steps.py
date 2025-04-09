from behave import when, then, given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.app.side_menu.click_sign_in_from_menu()


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page()


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_terms_condition()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.sign_in_page.verify_partial_url('terms-conditions')

@when('Enter {email}')
def enter_email(context, email):
    context.app.sign_in_page.input_text(email, By.CSS_SELECTOR, "input")
    context.app.sign_in_page.wait_until_clickable_click(By.CSS_SELECTOR, "#login")