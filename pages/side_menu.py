from selenium.webdriver.common.by import By

from pages.base_page import Page


class SideMenu(Page):
    SIDE_MENU_SIGNIN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def click_sign_in_from_menu(self):
        self.wait_until_clickable_click(*self.SIDE_MENU_SIGNIN)
