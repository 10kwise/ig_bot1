from ig_main import ig_bot

#give the path to the crome driver path
path = 'c:\\Users\Administrator\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe'
university_accounts =  [ 
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
# Original array with duplicates
university_abbreviations = [
    "Harvard", "Stanford", "MIT", "UCB", 
    "UCLA", "UTAustin", "Columbia", "NYU",
    "UF", "USC", "Yale", "Princeton",
    "Cambridge", "UW-Madison", "UNC", "Georgetown",
    "MSU", "UC Davis", "UIowa", "UOregon",
    "UArizona", "UW", "UC Irvine", "Duke",
    "Carnegie Mellon", "UC Berkeley (Science)", "UT Austin", "Penn State",
    "UC Santa Barbara", "NYU Stern", "Caltech", "USC Marshall",
    "Harvard Medical", "Northwestern", "Vanderbilt", "Dartmouth",
    "Boston University", "FSU", "Texas A&M", "UCLA Anderson", 
    "UCSD", "UMich", "UIUC", "ASU",
    "Rutgers", "UVA", "GWU", "BU",
    "UCSC", "UT Dallas", "IU Bloomington", "Rice",
    "CU Boulder", "UCR", "Emory", "UCSB",
    "UNLV", "USF", "KSU", "CU Denver",
    "UConn", "UMass", "LSU", "BYU",
    "VCU", "UCF", "Baylor", "Tulane",
    "UVM", "URI", "NCSU", "SDSU",
    "TCU", "CSUF", "UCM", "UCI",
    "UCO", "UMD", "UCR",
    "UTK", "UTSA", "UTEP", "UW",
    "UIC", "UC", "UCR", "UNCW",
    "UVA", "UT", "UNM", "UTK",
    "UCM", "UCSB", "UCR",
    "UCSD", "UCI", "UCO", "UMD",
    "UMD", "UIC", "UC" 
]

# Remove duplicates by converting to a set and back to a list
university_abbreviations = list(set(university_abbreviations))

#create a text document with the username in the  first sentence and password int the second sentence
#provide the path to the text file

path_txt =  'c:\\Users\Administrator\Desktop\word\login_dets.txt'
with open(path_txt) as login_dets:
    username = login_dets.readline()
    password = login_dets.readline()

bot = ig_bot(path=path,names=university_accounts,username=username,password=password,uni_abreviations=university_abbreviations)

bot.log_in()
bot.search(1)
