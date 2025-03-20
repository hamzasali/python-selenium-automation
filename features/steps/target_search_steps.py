from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(3)


@then('Verify correct search result')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    # print('Actual text:\n',actual_text)
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@when('Click on cart')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
    sleep(3)


@then('Verify cart is empty')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(3)


@when('Click Sign in from menu')
def click_sign_in_from_menu(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(3)


@then('Verify Sign in form opened')
def verify_sign_in_page(context):
    context.driver.find_element(By.ID, 'login')
    sleep(3)
    result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    expected = 'Sign into your Target account'
    assert expected in result
