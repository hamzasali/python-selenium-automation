from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADING = (By.CSS_SELECTOR, "[class*='styles_ndsHeading']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, '#login')
    TERM_CONDITIONS_BTN = (By.CSS_SELECTOR, "[data-behavior='redirectToSpotPage'][href*='terms-conditions']")

    def verify_sign_in_page(self):
        self.verify_text('Sign in or create account', *self.SIGN_IN_HEADING)
        self.find_element(*self.SIGN_IN_BTN)

    def click_terms_condition(self):
        self.wait_until_clickable_click(*self.TERM_CONDITIONS_BTN)
