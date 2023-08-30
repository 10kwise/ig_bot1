from ig_main import ig_bot

path = 'c:\\Users\Administrator\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'
bot = ig_bot(path=path)
try:
    bot.log_in()
    bot.find_follower()
except:
    print("error")
