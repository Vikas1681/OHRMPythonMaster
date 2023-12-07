
import pytest
import os, sys

# sys.path.insert(1, 'C://Users//u723399//eclipse-workspace//OHRM_SeleniumPythonMaster//Configurations//Constants.py')
# sys.path.insert(2, 'C://Users//u723399//eclipse-workspace//OHRM_SeleniumPythonMaster//Generics//InitialiseWebDriver.py')

from Generics.InitialiseWebDriver import InitialiseWebDriver
from Configurations.Constants import Constants

# from Generics.InitialiseWebDriver import InitialiseWebDriver
# from Configurations.Constants import Constants
# from Configurations import *

SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


@pytest.fixture(scope="class")
def setupTestEnvironment(request):
    
    strBrowserName = Constants.driver
    if strBrowserName not in SUPPORTED_BROWSERS:
        raise Exception(strBrowserName + " is not a supported browser")
    
    if strBrowserName == 'chrome':
        driver = InitialiseWebDriver().initialiseDriver(strBrowserName)
        driver.get(Constants.URL)
        driver.implicitly_wait(Constants.DEFAULT_WAIT)
        request.cls.driver = driver
    
