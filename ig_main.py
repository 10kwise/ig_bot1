from selenium import webdriver
import selenium
from selenium.webdriver.chrome.service import Service 
import time
import random

class ig_bot():
    def __init__(self,path:str,names:[],username:str,password:str,uni_abreviations:list) -> None:

        self.website = 'https://www.instagram.com/?hl=en'
        self.services= Service(path)
        self.password = password
        self.username = username
        self.uni_abreviations =uni_abreviations
        
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
        time.sleep(5)   
        self.driver.refresh() 
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

                #checks wheather the search input is selected to prevent deselecting it
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
                #if search input pox is not selected select it
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
            #if search window is not open click on search to open it
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
            self.get_into_followers(3)
    
    def get_into_followers(self,depth:int):
        #//input[@class="x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j"]
        #follower screen #//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]/div/div/div/div[2]/div/div/div/div/div/a
        #followers button #//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd"]
        
        #function that will be carried out in the follower page
        def act():
                follower.click()
                if(self.is_student(self.uni_abreviations)):
                    #implement what you want to do here

                    self.check_post(2)
                    print("student" + str(depth))              
                    if depth > 0: 
                        self.get_into_followers(depth=(depth-1))

                else:
                    pass
                time.sleep(2)
                self.driver.back()
        try:
            followers_button = self.driver.find_element(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd"]')
            followers_button.click()
            time.sleep(2)
            followers = self.driver.find_elements(by='xpath',value='//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]/div/div/div/div[2]/div/div/div/div/div/a')
            for follower in followers:
                act()
        except:
            followers = self.driver.find_elements(by='xpath',value='//div[@class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"]/div/div/div/div[2]/div/div/div/div/div/a')
            time.sleep(2)
            for follower in followers:
                act()
                
               
        

    def is_student(self,abreviations:list):
        bio = self.driver.find_element(by='xpath',value='//h1[@class="_aacl _aaco _aacu _aacx _aad6 _aade"]')
        bio = bio.text.split()
        for text in bio:
            for abv in abreviations:
                if abv == text:
                    return True
        return False
    
    def follow(self):
        follow_button = self.driver.find_element(by='xpath',value='//button[@class="_acan _acap _acas _aj1-"]')
        follow_button.click()
        
    
    def check_post(self,post_count:int):
        post = self.driver.find_element(by='xpath',value='//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd"]')
        post.click()
        count = post_count
        count -= 1
        while count > 0:
            next = self.driver.find_element(by='xpath',value='//button[@class="_abl-"]')
            time.sleep(2.5)
            #probability to like a post
            possibility = random.randint(1,10)
            if possibility <= 1:
                self.like()
            
            next.click()

        actions = webdriver.ActionChains(self.driver)
        actions.send_keys(webdriver.Keys.ESCAPE)
        actions.perform()
        time.sleep(1)

    def like(self):
        self.driver.find_element(by='xpath',value="//button[@type='button']//*[name()='svg' and @aria-label='Like' and @height='24']").click()
        

            





