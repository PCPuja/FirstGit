from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/PUJA/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
#LinkText -- to identify the link text we have to check the HTML if if is starting with tag a
#
driver.find_element(By.LINK_TEXT,'Forgot password?').click()
#xpath by travelling through tagname
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Puja@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Puja@1234")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()