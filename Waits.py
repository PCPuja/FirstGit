import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/PUJA/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
expectedlist=['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
#product_list:
actuallist=[]
productlist= driver.find_elements(By.XPATH,"//div/h4")
for product in productlist:
    actuallist.append(product.text)
print(actuallist)

assert actuallist == expectedlist

count = driver.find_elements(By.XPATH,"//div[@class='products']/div")
print(len(count))
assert len(count)>0
#Chaining of web element
for c in count:
    c.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#sum _validation
sum=0
rates= driver.find_elements(By.XPATH,"//tr/td[5]/p")
for rate in rates:
     sum= sum+int(rate.text)
print(sum)
totalamount= int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum == totalamount



driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
wait= WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

discountedamount= float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
print(discountedamount)
assert totalamount>discountedamount

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
dropdown= Select(driver.find_element(By.XPATH,"//div/select"))
dropdown.select_by_value("India")

driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
driver.find_element(By.XPATH,"//button[text()='Proceed']").click()






