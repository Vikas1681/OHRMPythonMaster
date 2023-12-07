from Generics.Basepage import BasePage
from Generics.Utility import Utility


class AdminPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.objUtility = Utility(driver)

    hdrAdminPage = "//div[@class='oxd-topbar-header-title']//h6[text()='Admin']"

    def verifyAdminPageDisplayed(self):
        self.objUtility.VerifyResults("verify admin page displayed",self.verifyPageDisplayed(self.hdrAdminPage))


