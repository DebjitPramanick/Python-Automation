from selenium import webdriver
import time
from confidential import username, password
driverLoc = 'Web Automation/chromedriver'

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(driverLoc)
        
    def login(self):
        self.driver.get('https://github.com')
        menu = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/button')
        menu.click()
        signin = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/div[2]')
        signin.click()

        for _ in range(3):
            usernameField = self.driver.find_element_by_xpath('//*[@id="login_field"]')
            usernameField.click()
            if usernameField.get_attribute('value') == '':
                usernameField.send_keys(username)

            pwdField = self.driver.find_element_by_xpath('//*[@id="password"]')
            pwdField.click()
            if pwdField.get_attribute('value') == '':
                pwdField.send_keys(password)
        
        
        

        signinBtn = self.driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]')
        signinBtn.click()

bot = Bot()
bot.login()