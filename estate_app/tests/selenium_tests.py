from selenium import webdriver
import unittest
import os

# os.environ['DJANGO_SETTINGS_MODULE'] = 'SoftUniPythonWebExamProject.settings'
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class ViewTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def login_user_Pesho(self, driver):

        driver.get("http://localhost:8000/auth/login/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('Pesho')
        login_password = driver.find_element_by_id('id_password')
        login_password.send_keys('Brum@123')
        enter_btn = driver.find_element_by_xpath('/html/body/div[2]/div/form/button')
        enter_btn.click()
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/")

    def test_open_home_page(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        self.assertIn("Real Estate", driver.title)

    def test_create_ad_page_loads_after_login_and_click_on_btn(self):
        driver = self.driver
        self.login_user_Pesho(driver)
        create_ad_btn = driver.find_element_by_class_name('create-ad')
        create_ad_btn.click()
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/create_ad/")

    def test_create_ad_ad_created_successfully(self):
        driver = self.driver
        self.login_user_Pesho(driver)
        driver.get("http://localhost:8000/create_ad/")
        sale_rent = Select(driver.find_element_by_id('id_sale_or_rent'))
        sale_rent.select_by_value('2')
        phone_num = driver.find_element_by_id('id_phone_number')
        phone_num.send_keys('1234567890')
        price = driver.find_element_by_id('id_price')
        price.send_keys('100000')
        district = Select(driver.find_element_by_id('id_district'))
        district.select_by_value('6')
        type_premise = Select(driver.find_element_by_id('id_type_premise'))
        type_premise.select_by_value('7')
        city = Select(driver.find_element_by_id('id_city'))
        city.select_by_visible_text('София')
        floor = driver.find_element_by_id('id_floor')
        floor.send_keys('2')
        area = Select(driver.find_element_by_id('id_area'))
        area.select_by_value('9')
        construction = Select(driver.find_element_by_id('id_construction'))
        construction.select_by_value('1')
        sqr_meters = driver.find_element_by_id('id_square_meters')
        sqr_meters.send_keys('100')
        total_floor = driver.find_element_by_id('id_total_floors')
        total_floor.send_keys('6')
        num_rooms =Select(driver.find_element_by_id('id_number_rooms'))
        num_rooms.select_by_value('3')
        furniture = Select(driver.find_element_by_id('id_furniture'))
        furniture.select_by_value('1')
        elevator = Select(driver.find_element_by_id('id_elevator'))
        elevator.select_by_value('1')
        description = driver.find_element_by_id('id_description')
        description.send_keys('Ad created from automation test purposes')
        btn_save = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[3]/div[1]/button')
        btn_save.click()
        location = driver.current_url
        self.assertIn('http://localhost:8000/details/', location)
        msg_ad_created = driver.find_element_by_xpath('/html/body/div[2]/section/h6')
        self.assertEqual('Обявата Ви e запазена. Когато бъде одобрена, ще бъде видима за всички.', msg_ad_created.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
