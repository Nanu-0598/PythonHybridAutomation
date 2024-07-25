import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.cutom_logs import Log_Maker


class Test_First_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalidusername()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("*********************First Test Case***********")
        self.logger.info("*********************Verification of Admin login Page***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        act_title = self.driver.title
        exp_title = "Your store. Login"
        if act_title == exp_title:
            self.logger.info("*********************First Test Cases is Passed***********")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("*********************First Test Cases is Failed***********")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.logger.info("*********************Second Test Case***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_on_login_button()
        act_dash_title = self.driver.find_element(By.XPATH,"//div[@class='content-header']/h1").text
        if act_dash_title == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self,setup):
        self.logger.info("*********************Third Test Case***********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_on_login_button()
        err_msg = self.driver.find_element(By.XPATH,"//li").text
        if err_msg == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False



