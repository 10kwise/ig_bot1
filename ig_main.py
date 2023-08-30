from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time
class ig_bot():
    def __init__(self,path:str,names:[]) -> None:
        self.website = 'https://www.instagram.com/?hl=en'
        self.services= Service(path)
        self.driver = webdriver.Chrome(service=self.services)
        # self.driver.fullscreen_window()
        self.driver.maximize_window()
        self.names = names
    
    def log_in(self):
        self.driver.get(self.website)
        #//input[@aria-label="Search input"]...... searchbar entry
        #//input[@aria-label="Phone number, username, or email"]......username entry
        #//input[@aria-label="Password"] .........password entry
        #//button[@class="_acan _acap _acas _aj1-"].........login button

        self.driver.implicitly_wait(6)

        username = self.driver.find_element(by='xpath',value='//input[@aria-label="Phone number, username, or email"]')
        username.click()
        #this is the username
        username.send_keys('')
        password = self.driver.find_element(by='xpath',value='//input[@aria-label="Password"]')
        password.click()
        #insert password
        password.send_keys('')
        login = self.driver.find_element(by='xpath',value='//button[@class="_acan _acap _acas _aj1-"]')
        login.click()
        time.sleep(5)
        self.driver.refresh()
        notifications = self.driver.find_element(by='xpath',value='//button[@class="_a9-- _a9_1"]')
        notifications.click()
        
        

    
#//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]
#^for the search button the third element
    def open_search(self,depth:int):
        self.driver.refresh()
        try:

            for user_name in self.names:
                
                    for i in range(depth):
                        search = self.driver.find_elements(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]'
                                                            )
                        search = search[2]
                        if(search.is_selected() == False):
                            print('click')
                            search.click()
                        # search = self.driver.find_element(by='xpath',value='//input[@class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]')
                        time.sleep(2)
                        # search_input = self.driver.find_element(by='xpath',value='//input[@class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]')
                                    # Create an instance of ActionChains
                        actions = webdriver.ActionChains(self.driver)
                        actions.send_keys(user_name)
                        actions.send_keys(webdriver.Keys.RETURN)
                        # Perform the actions
                        actions.perform()
                        time.sleep(3)
                        container = self.driver.find_elements(by='xpath',value='//div[@class="x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn"]/a')
                        container[i].click()
                        time.sleep(10)
                    
            
        except :
            print('problems emmerged')
        while True:
            if input('any    '):
                break
        
    def get_followers(self,depth:int,xpathob):
        #//input[@class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]

        pass



