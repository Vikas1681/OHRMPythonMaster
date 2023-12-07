from ObjectRepository.LoginPage import LoginPage
from Configurations.Constants import Constants

class LoginView:
    
    def __init__(self,driver):
        self.driver = driver
        self.objLoginPage = LoginPage(driver)
    
    
    def verifyLoginPageDispalyed(self):
        self.objLoginPage.verifyLoginPageDisplayed()
    
    def doLogin(self):

        self.objLoginPage.enterLoginPageUsername(Constants.Username)
        self.objLoginPage.enterLoginPagepassword(Constants.Password)
        self.objLoginPage.clickLoginPageLoginButton()
