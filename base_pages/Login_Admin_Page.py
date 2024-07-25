from selenium.webdriver.common.by import By

class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    logout_button_xpath = "(//div[@id='navbarText'])//ul//li[3]/a"

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
            self.driver.find_element(By.ID, self.textbox_username_id).clear()
            self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
            self.driver.find_element(By.ID, self.textbox_password_id).clear()
            self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_on_login_button(self):
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_on_logout_button(self):
            element = self.driver.find_element(By.XPATH, self.logout_button_xpath)
            self.driver.execute_script("arguments[0].click();", element)


