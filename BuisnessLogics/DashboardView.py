from ObjectRepository.DashboardPage import DashboardPage


class DashboardView:

    def __init__(self,driver):
        self.objDashboardPage= DashboardPage(driver)


    def verifyDashboardPageDisplayed(self):
        self.objDashboardPage.verifyDashboardPageDisplayed()

    def commonDashboardPageClickLHSLink(self):
        self.objDashboardPage.clickDashboardPageLHSLinks("Admin")


