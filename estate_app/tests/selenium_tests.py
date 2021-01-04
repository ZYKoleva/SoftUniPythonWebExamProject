from selenium import webdriver
import unittest

from selenium.webdriver import ActionChains
from seleniumrequests import Chrome
import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'SoftUniPythonWebExamProject.settings'
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException


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

    def login_superuser(self, driver):

        driver.get("http://localhost:8000/auth/login/")
        login_username = driver.find_element_by_id('id_username')
        login_username.send_keys('zoey')
        login_password = driver.find_element_by_id('id_password')
        login_password.send_keys('test')
        enter_btn = driver.find_element_by_xpath('/html/body/div[2]/div/form/button')
        enter_btn.click()
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/")

    def logout_user_Pesho(self, driver):

        enter_btn = driver.find_element_by_xpath('/html/body/div[1]/header/section/ul/li[2]/a')
        enter_btn.click()
        location = driver.current_url
        self.assertEqual(location, "http://localhost:8000/")

    def is_element_present(self, location, by_what, selector):
        driver = webdriver.Chrome()
        driver.get(location)
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(ec.presence_of_element_located((by_what, selector)))
        except TimeoutException:
            return False
        return True

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

    def test_create_ad_button_missing_if_user_not_logged(self):
        # webdriver = Chrome()
        # response = webdriver.request('GET', 'http://localhost:8000/')
        driver = self.driver
        driver.get('http://localhost:8000/')

        with self.assertRaises(Exception) as ex:
            driver.find_element_by_class_name('create-ad')
        self.assertIsNotNone(ex)

    def test_unlogged_user_access_create_ad_raise_error(self):
        driver = self.driver
        driver.get('http://localhost:8000/create_ad/')
        location = driver.current_url
        self.assertEqual('http://localhost:8000/auth/login/?next=/create_ad/', location)

    def test_superuser_login_create_btn_approve_btn_available(self):
        driver = self.driver
        self.login_superuser(driver)
        create_btn = driver.find_element_by_class_name('create-ad')
        self.assertIsNotNone(create_btn)
        approve_btn = driver.find_element_by_id('id_pending_approval')
        self.assertIsNotNone(approve_btn)

    def test_superuser_click_approve_btn_only_pending_approval_ads_load(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        self.login_superuser(driver)
        approve_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@type="checkbox"]')))
        search_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        approve_btn.click()
        search_btn.click()
        ads_per_page = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'card-body')))
        span_pending_approval = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'pending-approval')))
        self.assertEqual(len(ads_per_page), len(span_pending_approval))

    def test_superuser_approve_btn_available_on_ad_detail_page(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        self.login_superuser(driver)
        approve_btn_check = wait.until(ec.presence_of_element_located((By.XPATH, '//input[@type="checkbox"]')))
        search_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        approve_btn_check.click()
        search_btn.click()
        driver.maximize_window()
        details_btn = wait.until(ec.presence_of_element_located((By.XPATH,"//*[@class='btn-group']/a")))
        ActionChains(driver).move_to_element(details_btn).click(details_btn).perform()
        location = driver.current_url
        ad_id = location[len('http://localhost:8000/details/'): -1]
        self.assertEqual(f'http://localhost:8000/details/{ad_id}/', location)
        details_approve_btn = wait.until(ec.presence_of_element_located((By.ID, "details-approve-ad")))
        ActionChains(driver).move_to_element(details_approve_btn).click(details_approve_btn).perform()
        driver.refresh()
        btn_still_present = False
        try:
            btn_still_present = wait.until(ec.presence_of_element_located((By.ID, "details-approve-ad")))
        except TimeoutException:
            self.assertFalse(btn_still_present)
        self.assertEqual( f'http://localhost:8000/details/{ad_id}/', driver.current_url)
        driver.get('http://localhost:8000/auth/logout/')
        driver.get('http://localhost:8000/')
        ref_num_input_field = wait.until(ec.presence_of_element_located((By.ID, 'id_reference_number')))
        ref_num_input_field.send_keys(f'{ad_id}')
        search_btn = wait.until(ec.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        search_btn.click()
        approved_ad = wait.until(ec.presence_of_element_located((By.ID, ad_id)))
        self.assertIsNotNone(approved_ad)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
