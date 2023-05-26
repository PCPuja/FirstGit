from selenium.webdriver.common.by import By


class Logout:
    #driver.find_element(By.XPATH,"//div[@aria-label='Account controls and settings']/span")
    settingbutton =(By.XPATH,"//div[@aria-label='Account controls and settings']/span")
    #driver.find_element(By.XPATH, "//div/div/span[text()='Log Out']")
    logoutButton = (By.XPATH,"//div/div/span[text()='Log Out']")

    def __init__(self,driver):
        self.driver = driver

    def getsetting(self):
        return self.driver.find_element(*Logout.settingbutton)

    def getlogoutdetails(self):
        return self.driver.find_element(*Logout.logoutButton)
