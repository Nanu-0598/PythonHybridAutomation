import time

from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.cutom_logs import Log_Maker
from utilities import read_excel

class Test_First_Admin_Login_datadriven:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    path = ".//test_data//admin_login_data.xlsx"
    status_list = []


    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("*********************Data driven Test cases started***********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.admin_lp = Login_Admin_Page(self.driver)
        self.rows = read_excel.get_row_count(self.path,"Sheet1")
        print("num of rows", self.rows)

        for r in range(2,self.rows+1):
            self.username = read_excel.read_data(self.path,"Sheet1",r,1)
            self.password = read_excel.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = read_excel.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_on_login_button()
            time.sleep(5)
            act_dash_title = self.driver.title
            exp_dash_title = "Dashboard / nopcommerce administration"
            if act_dash_title == exp_dash_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")
                    self.driver.implicitly_wait(20)
                    self.admin_lp.click_on_logout_button()
                elif self.exp_login == "No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.driver.implicitly_wait(20)
                    self.admin_lp.click_on_logout_button()
            elif act_dash_title != exp_dash_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("fail")
                elif self.exp_login == "No":
                    self.logger.info("test data is passed")
                    self.status_list.append("pass")


        print("Status list is ", self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test is failed")
            assert False
        else:
            self.logger.info("Test admin data driven test is failed")
            assert True



