import pytest

from BuisnessLogics.DashboardView import DashboardView
from BuisnessLogics.LoginView import LoginView
@pytest.mark.usefixtures("setupTestEnvironment")
class TestLogin():

    @pytest.fixture()
    def initialiseViewsAndPages(self):
        self.objLoginView = LoginView(TestLogin.driver)
        self.objDashboardView = DashboardView(TestLogin.driver)

    def test_login(self,initialiseViewsAndPages):
        self.objLoginView.verifyLoginPageDispalyed()
        self.objLoginView.doLogin()
        self.objDashboardView.verifyDashboardPageDisplayed()
        self.objDashboardView.commonDashboardPageClickLHSLink()



    
    

