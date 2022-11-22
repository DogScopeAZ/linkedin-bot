# General bot settings

#PRO FEATURE - browser you want the bot to run ex: ["Chrome"] or ["Firefox"]. Firefox is only supported in Pro feature
browser = ["Chrome"]
# Enter your Linkedin password and username below. Do not commit this file after entering these credentials.
# Linkedin credentials
email = ""
password = ""

#PRO FEATURE - Optional! run browser in headless mode, no browser screen will be shown it will work in background.
headless = False
#PRO FEATURE - Optional! If you left above credentials fields empty. For Firefox or Chrome enter profile dir to run the bot without logging in your account each time
# get Firefox profile path by typing following url: about:profiles
#firefoxProfileRootDir = r"/home/ongun/snap/firefox/common/.mozilla/firefox/pz0eh58h.Linkedin_bot"
# get Chrome profile path by typing following url: chrome://version/
chromeProfilePath = r"C:\Users\USERHERE\AppData\Local\Google\Chrome\User Data\Default"

# location you want to search the jobs - ex : ["Poland", "Singapore", "New York City Metropolitan Area", "Monroe County"]
# continent locations:["Europe", "Asia", "Australia", "NorthAmerica", "SouthAmerica", "Africa", "Australia"]
location = ["United States"]
# keywords related with your job search
keywords = ["Information Security", "Director of Information Security", "Cyber Security", "Architect", "CISO", "Information Technology", "VP Information Security", "VP Information Technology", "cloud", "Cyber Security Analyst", "Cyber Security Engineer", "SOC", "Chief Information Security Officer", "Information Security Manager", "SOC Manager", "SOC Director"]
#job experience Level - ex:  ["Internship", "Entry level" , "Associate" , "Mid-Senior level" , "Director" , "Executive"]
experienceLevels = [ "Director" , "Mid-Senior level" , "Executive"]
#job posted date - ex: ["Any Time", "Past Month" , "Past Week" , "Past 24 hours"] - select only one
datePosted = ["Any Time"]
#job type - ex:  ["Full-time", "Part-time" , "Contract" , "Temporary", "Volunteer", "Intership", "Other"]
jobType = ["Full-time", "Part-time" , "Contract"]
#remote  - ex: ["On-site" , "Remote" , "Hybrid"]
remote = ["Remote"]
#salary - ex:["$40,000+", "$60,000+", "$80,000+", "$100,000+", "$120,000+", "$140,000+", "$160,000+", "$180,000+", "$200,000+" ] - select only one
salary = [ "$140,000+"]
#sort - ex:["Recent"] or ["Relevent"] - select only one
sort = ["Recent"]
#Blacklist companies you dont want to apply - ex: ["Apple","Google"]
blacklistCompanies = []
#Blaclist keywords in title - ex:["manager", ".Net"]
blackListTitles = ["sales"]
#Follow companies after sucessfull application True - yes, False - no
followCompanies = False

 # Testing features
displayWarnings = False