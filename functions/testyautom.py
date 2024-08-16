# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
login_username = driver.find_element(By.XPATH, "//input[@id='user-name']")
login_username.send_keys("standard_user")
login_password = driver.find_element(By.XPATH, "//input[@id='password']")
login_password.send_keys("secret_sauce")
login_button = driver.find_element(By.XPATH,"//input[@id='login-button']")
login_button.click()
product_label = driver.find_element(By.XPATH, "//span[@class='title']")
assert product_label.text == "Products"
time.sleep(2)


# //a[@class='shopping_cart_link']


 