from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, "[data-test=boxEmptyMsg]")

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        actual_text = self.find_element(*self.EMPTY_CART_MSG).text
        assert expected_text in actual_text, f'Expected "{expected_text}" but got "{actual_text}"'
