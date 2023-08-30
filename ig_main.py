from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time
class ig_bot():
    def __init__(self,path:str) -> None:
        self.website = 'https://www.instagram.com/?hl=en'
        self.services= Service(path)
        self.driver = webdriver.Chrome(service=self.services)
    
    def log_in(self):
        self.driver.get(self.website)
        #//input[@aria-label="Search input"]...... searchbar entry
        #//input[@aria-label="Phone number, username, or email"]......username entry
        #//input[@aria-label="Password"] .........password entry
        #//button[@class="_acan _acap _acas _aj1-"].........login button

        self.driver.implicitly_wait(6)

        username = self.driver.find_element(by='xpath',value='//input[@aria-label="Phone number, username, or email"]')
        username.click()
        username.send_keys('lily_json')
        password = self.driver.find_element(by='xpath',value='//input[@aria-label="Password"]')
        password.click()
        password.send_keys('lewismaps10kcorp')
        login = self.driver.find_element(by='xpath',value='//button[@class="_acan _acap _acas _aj1-"]')
        login.click()
        time.sleep(5)
        self.driver.refresh()
        notifications = self.driver.find_element(by='xpath',value='//button[@class="_a9-- _a9_1"]')
        notifications.click()
        
        

    
#//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]
#^for the search button the third element
    def open_search(self):
        self.driver.refresh()
        try:
            search = self.driver.find_elements(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]'
                                              )
            search[2].click()
            
        except :
            print('problems emmerged')
        while True:
            if input('any    '):
                break
        
    def get_followers():
        
        pass



