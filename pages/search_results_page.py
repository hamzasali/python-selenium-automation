from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*=addToCartButton]")

    def verify_search_result(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_results_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_add_to_cart(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)