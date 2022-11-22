# Linkedin Bot 

## Installation

- clone the repo
- Make sure Python and pip is installed
- Install dependencies with `pip3 install -r requirements.yaml`
- Enter your linkedin credentials on line 8 and 9 of config.py file
- Modify config.py according to your demands.
- Run `python3 linkedin.py`
- Check Applied Jobs DATA .txt file is generate under /data folder

## Tests

There is a specific test folder for you to test the dependencies, the bot and if everything is set up correctly. To do that I recommend,
running below codes,

1. Go to the tests folder run `python3 setupTests.py` this will output if Python,pip,selenium,dotenv and Firefox are installed correctly on your system.
2. Run `python3 seleniumTest.py` this will output if the Selenium and gecko driver is able to retrieve data from a website. If it returns an error make sure you have correctly installed selenium and gecko driver
3. Run `python3 linkedinTest.py` this will try to log in automatically to your Linkedin account based on the path you defined in the .env file. If its giving an error make sure the path exists and logged in manually to your Linkedin account once.


## How to Set up

This tutorial briefly explains how to set up LinkedIn Easy Apply jobs bot. With few modifications you can make your own bot or try my other bots for other platforms.

1. Install Chrome.
2. Install Python.
3. Download Geckodriver put it in Python’s installation folder.
4. Install pip, python get-pip.py
5. Install selenium pip install selenium
6. Clone the code
7. Launch new profile, go Linkedin.com and log in your account.
8. Modify/adapt the code and run
9. After each run check the jobs that the bot didn’t apply automatically, apply them manually by saving your preferences
10. Next time the bot will apply for more jobs based on your saved preferences on Linkedin.
