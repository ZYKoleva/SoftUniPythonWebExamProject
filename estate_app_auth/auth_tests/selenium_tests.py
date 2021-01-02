from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class RegisterLoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1_register_page_loads(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        login_link = driver.find_element_by_xpath('/html/body/div[1]/header/section/ul/li[1]/a')
        login_link.send_keys(Keys.ENTER)
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/auth/register/")

    def test_2_successful_register_user_homePage_loads(self):
        driver = self.driver
        driver.get("http://localhost:8000/auth/register/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Gosho2')
        login_password1 = driver.find_element_by_id('id_password1')
        login_password1.send_keys('Brum@123')
        login_password2 = driver.find_element_by_id('id_password2')
        login_password2.send_keys('Brum@123')
        button_to_click = driver.find_element_by_class_name('btn-register-submit')
        button_to_click.click()

        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/")

        span_user_name = driver.find_element_by_xpath('/html/body/div[1]/header/section/ul/li[1]/span')
        self.assertEqual(span_user_name.text, 'Gosho2')

    def test_3_register_username_already_exists_message_appears(self):
        driver = self.driver
        driver.get("http://localhost:8000/auth/register/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Gosho2')
        login_password1 = driver.find_element_by_id('id_password1')
        login_password1.send_keys('Brum@123')
        login_password2 = driver.find_element_by_id('id_password2')
        login_password2.send_keys('Brum@123')
        button_to_click = driver.find_element_by_class_name('btn-register-submit')
        button_to_click.click()

        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/auth/register/")

        error_msg = driver.find_element_by_xpath('/html/body/div[2]/div/form/div/p[1]')
        isErrorMsgDisplayed = error_msg.is_displayed()
        self.assertTrue(isErrorMsgDisplayed)
        self.assertEqual('Потребителското име вече е заето. Моля изберете друго потребителско име', error_msg.text)

    def test_4_register_username_psws_dont_match_message_appears(self):
        driver = self.driver
        driver.get("http://localhost:8000/auth/register/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Gosho3')
        login_password1 = driver.find_element_by_id('id_password1')
        login_password1.send_keys('Brum@123')
        login_password2 = driver.find_element_by_id('id_password2')
        login_password2.send_keys('Brum@456')
        button_to_click = driver.find_element_by_class_name('btn-register-submit')
        button_to_click.click()

        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/auth/register/")

        error_msg = driver.find_element_by_xpath('/html/body/div[2]/div/form/div/p[2]')
        isErrorMsgDisplayed = error_msg.is_displayed()
        self.assertTrue(isErrorMsgDisplayed)
        self.assertEqual('Паролите не съвпадат. Моля въведете ги отново.', error_msg.text)

    def test_5_login_page_loads(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        login_link = driver.find_element_by_xpath('/html/body/div[1]/header/section/ul/li[2]/a')
        login_link.send_keys(Keys.ENTER)
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/auth/login/")

    def test_6_user_able_to_log_proper_credentials(self):
        driver = self.driver
        driver.get("http://localhost:8000/auth/login/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Gosho2')
        login_password = driver.find_element_by_id('id_password')
        login_password.send_keys('Brum@123')
        enter_btn = driver.find_element_by_xpath('/html/body/div[2]/div/form/button')
        enter_btn.click()
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/")
        span_user_name = driver.find_element_by_xpath('/html/body/div[1]/header/section/ul/li[1]/span')
        self.assertEqual(span_user_name.text, 'Gosho2')

    def test_7_user_login_incorrectPsw_errorMsg(self):
        driver = self.driver
        driver.get("http://localhost:8000/auth/login/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Gosho2')
        login_password = driver.find_element_by_id('id_password')
        login_password.send_keys('WrongPassword')
        buttonToClick = driver.find_element_by_class_name('btn-register-submit')
        buttonToClick.click()
        error_msg = driver.find_element_by_class_name('error-messages-text')
        isErrorMsgDisplayed = error_msg.is_displayed()
        self.assertTrue(isErrorMsgDisplayed)
        self.assertEqual('Потребителското име и/или паролата не съвпадат. Моля опитайте пак', error_msg.text)
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/auth/login/")

    def test_8_user_login_EmptyPsw_errorMsg(self):
        driver = self.driver
        driver.get("http://localhost:8000/auth/login/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Gosho2')
        login_password = driver.find_element_by_id('id_password')
        login_password.send_keys('')
        button_to_click = driver.find_element_by_class_name('btn-register-submit')
        button_to_click.click()

        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/auth/login/")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
