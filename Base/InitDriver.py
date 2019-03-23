from selenium import webdriver
from Library import ConfigReader

def startBrowser():
    global driver
    options=webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    #if ((ConfigReader.readConfigData("Details","driver"))=="chrome"):
    #path="C:\\Users\\meifute\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    path="../Driver/chromedriver.exe"
    driver = webdriver.Chrome(options=options,executable_path=path)
    #driver=webdriver.Chrome(executable_path=path)
    #elif ((ConfigReader.readConfigData("Details","driver"))=="firefox"):
    ## path = "C:\\Users\\meifute\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
    #driver = webdriver.Chrome(executable_path=path)
    driver.get(ConfigReader.readConfigData("Details","Application_url"))
    driver.maximize_window()
    return driver
def closeBrowser():
    driver.close()