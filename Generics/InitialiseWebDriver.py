from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class InitialiseWebDriver:
    
    driver = None

    def initialiseDriver(self, strBrowserName):
        
        if strBrowserName == 'chrome':
            objOptions = Options()
            objOptions.add_argument("--disable-notifications")
            objOptions.add_argument("--start-maximized")
#             objOptions.add_argument("ignore-certificate-errors")
            self.driver = webdriver.Chrome(options=objOptions)
            
            return self.driver
        
        else:
            return self.driver

