from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div[aria-label*='olor ']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(10)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    # expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    expected_colors = ['dark khaki', 'grey', 'navy/tan', 'white/sand/tan', 'black/gum', 'white/navy/red']
    # expected_colors = ['black/off white', 'black/white/gum', 'off white/grey', 'tan/off white',
    #                    'white/black/cement/gum']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        if 'Out of Stock' not in selected_color:
            actual_colors.append(selected_color)
        else:
            actual_colors.append(selected_color.split(' ')[0])
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
