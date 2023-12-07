from Generics.Basepage import BasePage
from Generics.Utility import Utility


class DashboardPage(BasePage):


    def __init__(self,driver):
        super().__init__(driver)
        self.objUtility = Utility(driver)

    hdrDashboardPage = "//h6[text()='Dashboard']"

    def verifyDashboardPageDisplayed(self):
        self.objUtility.VerifyResults("verify Dashboard Page Displayed",self.verifyPageDisplayed(self.hdrDashboardPage))

    def clickDashboardPageLHSLinks(self,strLnkName):
        lnkLHS = "//ul[@class='oxd-main-menu']/li/a/span[text()='"+strLnkName+"']"
        self.objUtility.VerifyResults("click on LHS links",self.clickOnElement(lnkLHS))




