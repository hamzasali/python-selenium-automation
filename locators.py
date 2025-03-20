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
driver.get('https://www.amazon.com/')


# By ID

driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, "nav-search-submit-button")

# By Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']") #//tag[@attribute='value']
driver.find_element(By.XPATH, "//input[@role='searchbox']")


# By Xpath, multiple attribute
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @role='searchbox']")
driver.find_element(By.XPATH, "//input[@name='field-keywords' and @tabindex='0' and @role='searchbox']")

# By Xpath without a tag  * = anytag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']") #//tag[@attribute='value']


# By Xpath with text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

#partial text match
driver.find_element(By.XPATH, "//h2[contains(text(),'Luxury')]")
