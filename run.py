from ig_main import ig_bot

#give the path to the crome driver path
path = 'c:\\Users\Administrator\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'
university_accounts =  [
    "mitpics", "ucberkeleyofficial", 
    "ucla", "utaustintx", "columbia", "nyuniversity",
    "uflorida", "uscedu", "yale", "princeton_university",
    "cambridgeuniversity", "uwmadison", "uncchapelhill", "georgetownuniversity",
    "michiganstateu", "ucdavis", "uiowa", "uoregon",
    "universityofarizona", "uofwa", "ucirvine", "dukeuniversity",
    "carnegiemellon", "ucberkeleyscience", "utaustintx", "penn_state",
    "ucsantabarbara", "nyustern", "caltechedu", "uscmarshall",
    "harvardmed", "northwesternu", "vanderbiltu", "dartmouthcollege",
    "bostonu", "floridastateuniversity", "texas.aandm", "uclaanderson",  
]

#create a text document with the username in the  first sentence and password int the second sentence
#provide the path to the text file

path_txt =  'c:\\Users\Administrator\Desktop\word\login_dets.txt'
with open(path_txt) as login_dets:
    username = login_dets.readline()
    password = login_dets.readline()

bot = ig_bot(path=path,names=university_accounts,username=username,password=password)
try:
    bot.log_in()
    bot.search(1)
except:
    print("error")
