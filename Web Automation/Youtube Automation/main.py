from selenium import webdriver

driverLoc = 'Web Automation/chromedriver'

class Music():
    def __init__(self):
        self.driver = webdriver.Chrome(driverLoc)
    
    def play(self):
        name = input("Enter a youtube channel name: ")
        self.driver.get('https://www.youtube.com/user/'+name+'/videos')
        new = self.driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[1]')
        new.click()

bot = Music()
bot.play()