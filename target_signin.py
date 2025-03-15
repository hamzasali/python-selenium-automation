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
driver.get('https://www.target.com/')

driver.find_element(By.ID, 'account-sign-in').click()
sleep(3)

driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(3)

driver.find_element(By.ID, 'login')
sleep(3)
result = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
expected = 'Sign into your Target account'
assert expected in result, f'Error. Text {expected} not in {result}'


sleep(3)
