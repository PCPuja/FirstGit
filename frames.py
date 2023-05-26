from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service("C:/Users/PUJA/chromedriver")
driver= webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element(By.LINK_TEXT,"iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("hey I have automated this frame !!")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)
      


