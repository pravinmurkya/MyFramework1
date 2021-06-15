import time

import pytest
from selenium.webdriver.common.by import By


class HomePageObject:

    def __init__(self, driver):
        self.driver = driver

    txt = (By.XPATH, "//span[@class = 'text']")
    uname = (By.ID, "userName")
    email = (By.ID, "userEmail")
    caddress = (By.ID, "currentAddress")
    paradd = (By.ID, "permanentAddress")
    submit = (By.ID, "submit")
    chks = (By.ID, "output")

    def test_element(self):
        return self.driver.find_element(*HomePageObject.txt)
    def test_uname(self):
        return self.driver.find_element(*HomePageObject.uname)

    def test_email(self):
        return self.driver.find_element(*HomePageObject.email)

    def test_caddress(self):
        return self.driver.find_element(*HomePageObject.caddress)

    def test_paddress(self):
        return self.driver.find_element(*HomePageObject.paradd)
    time.sleep(3)

    def test_submit(self):
        q = self.driver.find_element(*HomePageObject.submit)
        self.driver.execute_script("arguments[0].click();", q)

    time.sleep(5)
    @pytest.fixture(params=[
            {"username": "navin", "email": "navin@choo.com", "caddr": "go what-ever then right then again left ok",
            "paddr": "left then right then again left ok"},
            {"username": "pravin", "email": "emailzx@choo.com", "caddr": "left then right then again left ok",
            "paddr": "left then right then again left ok"}])


    def getdataz(self, request):
        return request.param
