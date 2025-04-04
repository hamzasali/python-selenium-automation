from selenium.webdriver.common.by import By

from pages.base_page import Page


class SideMenu(Page):
    SIDE_MENU_SIGNIN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper']  [id*=addToCart]")

    def click_sign_in_from_menu(self):
        self.wait_until_clickable_click(*self.SIDE_MENU_SIGNIN)

    def store_product_name(self):
       return self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text

    def click_add_to_cart_from_menu(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN_SIDE_NAV)
