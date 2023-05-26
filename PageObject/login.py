from selenium.webdriver.common.by import By


class Login:
    #self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("puja123@gmail.com")
    username = (By.CSS_SELECTOR,"input[name='email']")
    #self.driver.find_element(By.CSS_SELECTOR,"input[id='pass']")
    password =(By.CSS_SELECTOR,"input[id='pass']")
    #self.driver.find_element(By.NAME,"login")
    button = (By.NAME,"login")
    #driver.find_element(By.CSS_SELECTOR,"div[class='_9ay7']")
    message =( By.CSS_SELECTOR,"div[class='_9ay7']" )

    def __init__(self,driver):
        self.driver = driver

    def getlogindetails(self):

       return self.driver.find_element(*Login.username)
    def getpassword(self):
        return  self.driver.find_element(*Login.password)

    def getsubmitbutton(self):
        return  self.driver.find_element(*Login.button)

    def getmeassage(self):
        return self.driver.find_element(*Login.message)


