from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.side_menu import SideMenu
from pages.sign_in_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.help_page import HelpPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_menu = SideMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.help_page = HelpPage(driver)
