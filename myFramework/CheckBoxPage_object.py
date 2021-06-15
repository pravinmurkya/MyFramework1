from selenium.webdriver.common.by import By


class Chkbox:

    def __init__(self, driver):
        self.driver = driver

    chkclik = (By.XPATH, "//span[@class = 'text']")
    homechk = (By.XPATH, "//span[@class = 'rct-title']")
    togle = (By.CLASS_NAME, "rct-icon-expand-close")
    result = (By.ID, "result")
    def test_chkclik(self):
        print("Huurreee pravin")
        all = self.driver.find_elements(*Chkbox.chkclik)
        for i in all:
            if i.text == "Check Box":
                i.click()
                break

    def test_homechk(self):
        return self.driver.find_element(*Chkbox.homechk)

    def test_result(self):
        return self.driver.find_element(*Chkbox.result)

    def test_toggle(self):
        return self.driver.find_element(*Chkbox.togle)