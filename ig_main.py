from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service 
import time
class ig_bot():
    def __init__(self,path:str,names:[],username:str,password:str) -> None:

        self.website = 'https://www.instagram.com/?hl=en'
        self.services= Service(path)
        self.password = password
        self.username = username
        
        self.driver = webdriver.Chrome(service=self.services)
        self.driver.maximize_window()
        self.names = names
    
    def log_in(self):
        #//input[@aria-label="Search input"]...... searchbar entry
        #//input[@aria-label="Phone number, username, or email"]......username entry
        #//input[@aria-label="Password"] .........password entry
        #//button[@class="_acan _acap _acas _aj1-"].........login button

        self.driver.implicitly_wait(15)

        self.driver.get(self.website)
        try:
            #this inserts the username
            username = self.driver.find_element(by='xpath',value='//input[@aria-label="Phone number, username, or email"]')
            username.click()
            username.send_keys(self.username)

            #this inserts the password
            password = self.driver.find_element(by='xpath',value='//input[@aria-label="Password"]')
            password.click()
            password.send_keys(self.password)

            #this clicks on the login button
            login = self.driver.find_element(by='xpath',value='//button[@class="_acan _acap _acas _aj1-"]')
            login.click()
        except:
            pass


#//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]
#^for the search button the third element


    def search(self,depth:int): 
        #checks to see wheather we have truly opened the home page       
        try:
            time.sleep(2)   
            #some times the save info dialog appears handles that
            try:
                skip_save = self.driver.find_element(by='xpath',value='//button[@class="_acan _acap _acas _aj1-"]')
                skip_save.click()
                self.driver.refresh()

            except:
                pass

            search = self.driver.find_elements(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]'
                                                    )
            search[2].click()
            print ('got')
        except:
            self.driver.refresh() 
            time.sleep(2)   
            #some times the save info dialog appears handles that
            try:
                skip_save = self.driver.find_element(by='xpath',value='//button[@class="_acan _acap _acas _aj1-"]')
                skip_save.click()
                self.driver.refresh()
                
            except:
                pass
            #check wheather the notification function is showing if so disallow if not pass
            try:
                notifications = self.driver.find_element(by='xpath',value='//button[@class="_a9-- _a9_1"]')
                notifications.click()
            except:
                pass
            #refresh the page then grab the search button
            search = self.driver.find_elements(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]'
                                                )
            search = search[2]  
            #takes the list of accounts and searches for each 
            for user_name in self.names:
                #checks wheather the search window is open before searching
                try:
                    search_window = self.driver.find_element(by='xpath',value='//div[@class="_aaw6"]')
                    search_input = self.driver.find_element(by='xpath',value='//input[@class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]')

                    
                    if(search_input.is_selected()):
                        search_input.clear()
                        search_input.click()
                        time.sleep(1)
                        actions = webdriver.ActionChains(self.driver)
                        actions.send_keys(user_name)
                        actions.send_keys(webdriver.Keys.RETURN)    
                        actions.perform()   
                        time.sleep(2)
                        container = self.driver.find_elements(by='xpath',value='//div[@class="x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn"]/a')
                        if len(container) > 0:
                            container[0].click()
                            time.sleep(5) 
                            print('dont click')
                        else:
                            pass
                    else:
                        search_input.click()
                        search_input.clear()
                        search_input.click()
                        time.sleep(1)
                        actions = webdriver.ActionChains(self.driver)
                        actions.send_keys(user_name)
                        actions.send_keys(webdriver.Keys.RETURN)    
                        actions.perform()   
                        time.sleep(1)
                        container = self.driver.find_elements(by='xpath',value='//div[@class="x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn"]/a')
                        container[0].click()
                        time.sleep(6) 

                except:                    
                    search = self.driver.find_elements(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]'
                                                        )
                    search = search[2] 
                    search.click()
                    actions = webdriver.ActionChains(self.driver)
                    actions.send_keys(user_name)
                    actions.send_keys(webdriver.Keys.RETURN)    
                    actions.perform()   
                    time.sleep(2)
                    container = self.driver.find_elements(by='xpath',value='//div[@class="x9f619 x78zum5 xdt5ytf x1iyjqo2 x6ikm8r x1odjw0f xh8yej3 xocp1fn"]/a')
                    container[0].click()
                    time.sleep(6) 


        while True:
            if input('any    '):
                break
        
    def get_followers(self,depth:int,xpathob):
        #//input[@class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]

        pass



