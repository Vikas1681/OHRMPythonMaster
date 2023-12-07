import pytest
from Configurations.Constants import Constants
class Utility:
    
    strScreenshotPath = Constants.Project_Path+"//Screenshots"
    def __init__(self, driver):
        self.driver = driver
    
    def addAssertAndTakeScreenshot(self,strStep,boolResult):
        print(strStep)
        if boolResult:
            assert True
        else:
            self.driver.save_screenshot(self.strScreenshotPath+"Test.png")
            assert False
            
        
    def VerifyResults(self,log,boolResult):
        self.addAssertAndTakeScreenshot(log, boolResult)
