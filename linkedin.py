import time,math,random,os
import utils,constants,config

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import prRed,prYellow,prGreen

from webdriver_manager.chrome import ChromeDriverManager

class Linkedin:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
        prYellow("Trying to log in linkedin.")
        
        self.driver.find_element("id","username").send_keys(config.email)
        time.sleep(5)
        self.driver.find_element("id","password").send_keys(config.password)
        time.sleep(5)
        self.driver.find_element("xpath",'//*[@id="organic-div"]/form/div[3]/button').click()

    def generateUrls(self):
        with os.scandir('data') as it:
            if not any(it):
                os.mkdir('data')
        with open('data/urlData.txt', 'w', encoding="utf-8") as file:
            linkedinJobLinks = utils.LinkedinUrlGenerate().generateUrlLinks()
            for url in linkedinJobLinks:
                file.write(f"{url}\n")
            prGreen("Urls are created successfully, now the bot will visit those urls.")
    def linkJobApply(self):
        self.generateUrls()
        countApplied = 0
        countJobs = 0

                with open('data/urlData.txt') as urlData:
            for url in urlData:        
                self.driver.get(url)

                totalJobs = self.driver.find_element(By.XPATH,'//small').text 
                totalPages = constants.jobsPerPage * math.ceil(int(totalJobs) / constants.jobsPerPage)

                urlWords =  utils.urlToKeywords(url)
                lineToWrite = f"\nCategory: {urlWords[0]}, Location: {urlWords[1]}, Applying {str(totalJobs)} jobs."
                self.displayWriteResults(lineToWrite)

                for page in range(totalPages):
                    currentPageJobs = constants.jobsPerPage * page
                    url = f"{url}&start={currentPageJobs}"
                    self.driver.get(url)
                    time.sleep(random.uniform(1, constants.botSpeed))

                    offersPerPage = self.driver.find_elements(By.XPATH,'//li[@data-occludable-job-id]')

                    offerIds = [int(offer.get_attribute("data-occludable-job-id").split(":")[-1]) for offer in offersPerPage]

                    for jobID in offerIds:
                        offerPage = f"https://www.linkedin.com/jobs/view/{str(jobID)}"
                        self.driver.get(offerPage)
                        time.sleep(random.uniform(1, constants.botSpeed))

                        countJobs += 1

                        jobProperties = self.getJobProperties(countJobs)
                        if "blacklisted" in jobProperties: 
                            lineToWrite = f"{jobProperties} | * 🤬 Blacklisted Job, skipped!: {str(offerPage)}"
                            self.displayWriteResults(lineToWrite)
                        else :                    
                            button = self.easyApplyButton()

                            if button is not False:
                                button.click()
                                time.sleep(random.uniform(1, constants.botSpeed))
                                countApplied += 1
                                try:
                                    self.driver.find_element(By.XPATH,'//*[@id="job-details"]/div[2]/button[2]').click() # 90
                                                                        lineToWrite = "* ✅ Successful application. (EasyApply)" + str(offerPage)
                                    self.displayWriteResults(lineToWrite)
                                except:
                                    prRed("* ❌ Could not apply via easy apply.")
                            else:
                                lineToWrite = "* ❌ Could not apply via easy apply" + str(offerPage)
                                self.displayWriteResults(lineToWrite)

        totalSummary = "\n\nTotal Applied: " + str(countApplied) + " Total Jobs: " + str(countJobs)
        self.displayWriteResults(totalSummary)

        def getJobProperties(self,countJobs):
        jobProperties = ""

        try:
            jobTitle = self.driver.find_element(By.XPATH,'//*[@id="job-details"]/div[1]/h1').text
            jobProperties += " | JobTitle: " + str(jobTitle)
        except:
            jobProperties += " | JobTitle: Not Found"

        try:
            companyName = self.driver.find_element(By.XPATH,'//*[@id="job-details"]/div[1]/h3[1]/a').text
            jobProperties += " | CompanyName: " + str(companyName)
        except:
            jobProperties += " | CompanyName: Not Found"

        try:
            jobLocation = self.driver.find_element(By.XPATH,'//*[@id="job-details"]/div[1]/h3[2]/span[2]').text
            jobProperties += " | JobLocation: " + str(jobLocation)
        except:
            jobProperties += " | JobLocation: Not Found"

        try:
            jobDescription = self.driver.find_element(By.XPATH,'//*[@id="job-details"]/div[2]/div').text
            jobProperties += " | JobDescription: " + str(jobDescription)
        except:
            jobProperties += " | JobDescription: Not Found"

        try:
            blacklisted = utils.checkBlackList(jobTitle,companyName,jobLocation,jobDescription)
            jobProperties += " | Blacklisted: " + str(blacklisted)
        except:
            jobProperties += " | Blacklisted: Not Found" #150
        return jobProperties

    def easyApplyButton(self):
        try:
            return self.driver.find_element(By.XPATH,'//*[@id="job-details"]/div[2]/button[1]')
        except:
            return False

    def displayWriteResults(self,lineToWrite):
        print(lineToWrite)
        with open('jobResults.txt','a',encoding="utf-8") as file:
            file.write(lineToWrite)

