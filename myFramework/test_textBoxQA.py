import time

import pytest
from selenium.webdriver.common.by import By

from init.BaseClass import TestBaseClass
from myFramework.TextBoxPage_Object import HomePageObject

@pytest.mark.usefixtures("setup")
class Testmyframework1(TestBaseClass):

    def test_homePageAction(self, getdataz):
        log = self.getLogger()
        homepage = HomePageObject(self.driver)
        homepage.test_element().click()
        time.sleep(5)
        homepage.test_uname().send_keys(getdataz["username"])
        homepage.test_email().send_keys(getdataz["email"])
        homepage.test_caddress().send_keys(getdataz["caddr"])
        homepage.test_paddress().send_keys(getdataz["paddr"])
        time.sleep(3)
        q = self.driver.find_element(*HomePageObject.submit)
        self.driver.execute_script("arguments[0].click();", q)
        time.sleep(5)
        log.info("this is to inform you, we are in textbox execution")
        log.info(self.driver.find_element(By.XPATH, "//div/div/p[@id ='name']").text)
        log.info(self.driver.find_element(By.XPATH, "//div/div/p[@id ='email']").text)
        log.info(self.driver.find_element(By.XPATH, "//div/div/p[@id ='currentAddress']").text)
        log.info(self.driver.find_element(By.XPATH, "//div/div/p[@id ='permanentAddress']").text)
        self.driver.refresh()

    @pytest.fixture(params=[
        {"username": "navin", "email": "navin@choo.com", "caddr": "go what-ever then right then again left ok",
         "paddr": "left then right then again left ok"},
        {"username": "pravin", "email": "emailzx@choo.com", "caddr": "left then right then again left ok",
         "paddr": "left then right then again left ok"}])
    def getdataz(self, request):
        return request.param

