from Generics.Basepage import BasePage
from Generics.Utility import Utility
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.objUtility = Utility(driver)

    
    hdrLoginPage = "//div/img[@alt='company-branding']"
    inpUsername = "//input[@name='username']"
    inpPassword = "//input[@name='password']"
    btnLogin = "//button[@type='submit']"
    
    def verifyLoginPageDisplayed(self):
        self.objUtility.VerifyResults("verify login Page Displayed",self.verifyPageDisplayed(self.hdrLoginPage))
    
    def enterLoginPageUsername(self, strName):
        self.objUtility.VerifyResults("enter username on login Page",self.enterText(self.inpUsername, strName))

    def enterLoginPagepassword(self, strPass):
        self.objUtility.VerifyResults("enter password on login Page",self.enterText(self.inpPassword, strPass))
    
    def clickLoginPageLoginButton(self):
        self.objUtility.VerifyResults("click on login button",self.clickOnElement(self.btnLogin))

        
