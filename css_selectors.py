from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

# CSS, by ID = #
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox') # (By.ID, 'twotabsearchtextbox')
# CSS, by ID and tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# CSS by class = .
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us")
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us.icp-nav-flag")
# CSS by class and tag
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag-us.icp-nav-flag")

# CSS by tag, id, class
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive-attribute")

# CSS, by attribute => []

driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords'][aria-label='Search Amazon']")
# by tag and attribute
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords'][aria-label='Search Amazon']")

# by class and attribute
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute[name='field-keywords'][aria-label='Search Amazon']")
# by tag, class, attribute
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute[name='field-keywords'][aria-label='Search Amazon']")

# CSS, by attribute, contains => *=[]
driver.find_element(By.CSS_SELECTOR, "[aria-label*='Amazon']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsButtonPrimary'][class*='styles_ndsBaseButton']")
driver.find_element(By.CSS_SELECTOR, "[data-test=accountNav-signIn]")

# CSS, going from parent to child class use double space

