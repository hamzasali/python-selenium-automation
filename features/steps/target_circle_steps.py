from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, ".cell-item-content")

@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify at least {number_of_cells} benefit cell')
def verify_benefit(context, number_of_cells):
    number_of_cells = int(number_of_cells)
    num_cells = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(num_cells) >= number_of_cells, f"Number of cells should be at least {number_of_cells}"
