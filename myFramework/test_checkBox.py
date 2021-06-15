import time

import pytest

from init.BaseClass import TestBaseClass
from myFramework.CheckBoxPage_object import Chkbox


@pytest.mark.usefixtures("setup")
class TestCheckBox(TestBaseClass):

    def test_chkbox(self):
        chkbx = Chkbox(self.driver)
        chkbx.test_chkclik()
        chkbx.test_homechk().click()
        print(chkbx.test_result().text)
        chkbx.test_toggle().click()
       # chkbx.test_desktop().click()

        time.sleep(5)