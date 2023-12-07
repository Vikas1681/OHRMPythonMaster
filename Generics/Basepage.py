import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configurations.Constants import Constants




class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    
    def waitForPresenceOfelement(self, locator):
        return WebDriverWait(self.driver, Constants.DEFAULT_WAIT).until(EC.presence_of_element_located((By.XPATH,locator)))
        # return WebDriverWait(self.driver, Constants.DEFAULT_WAIT).until(EC.presence_of_element_located(locator))
    
    def clickOnElement(self, locator):
        try:
            element=self.waitForPresenceOfelement(locator)
            element.click()
            self.waitAfterEachAction(1)
            # self.driver.find_element(By.XPATH,locator).click()
            return True
        except Exception as e:
            print("exception info..,", e)
            return False
    
    def verifyPageDisplayed(self, locator):
        try:
            element=self.waitForPresenceOfelement(locator)
            print("element found")
            element.is_displayed()
            # self.driver.find_element(By.XPATH, locator).isDisplayed()
            # self.driver.find_element(By.XPATH,locator).isDisplayed()

            return True
        except Exception as e:
            print("exception info..,", e)
            return False
    
    def enterText(self,locator,strText):
        try:
            self.waitForPresenceOfelement(locator)
            # self.driver.find_element(self,By.XPATH,locator).send_keys(self,strText)
            self.driver.find_element(By.XPATH,locator).send_keys(strText)
            self.waitAfterEachAction(1)
            return True
        except Exception as e:
            print("exception info..,", e)
            return False

    def waitAfterEachAction(self,timer):
        time.sleep(timer)

    def commonSelectDateFromDatePicker(self):
        iconFromDateCalendar = "//label[text()='From Date']/parent::div/following-sibling::div//i[@class='oxd-icon bi-calendar oxd-date-input-icon']"
        self.clickOnElement(iconFromDateCalendar)


    
    
        
