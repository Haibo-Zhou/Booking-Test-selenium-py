import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SearchHotel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navi to Booking.com
        cls.driver.get('https://www.booking.com/')

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def test_01_Search_location(self):
        # find search field for locations
        search_field = self.driver.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys('Auckland')
        time.sleep(1)

        self.assertEqual('Auckland', search_field.get_attribute('value'))

    def test_02_check_in_out(self):
        # enter check-in day
        check_in = self.driver.find_element_by_css_selector('.xp__dates-inner.xp__dates__checkin')
        check_in.click()
        time.sleep(1)

        check_in_day = self.driver.find_element_by_css_selector("td[data-date='2019-07-20']")
        check_in_day.click()
        time.sleep(1)

        # check if select day is "Sat, Jul 20"
        check_in_sel_day = check_in.find_element_by_class_name('sb-date-field__display')
        self.assertEqual("Sat, Jul 20", check_in_sel_day.text)

        # enter check-out day
        check_out_day = self.driver.find_element_by_css_selector("td[data-date='2019-07-27']")
        check_out_day.click()
        time.sleep(1)

        # check if select day is "Sat, Jul 27"
        check_out = self.driver.find_element_by_css_selector('.xp__dates-inner.xp__dates__checkout')
        check_out_sel_day = check_out.find_element_by_class_name('sb-date-field__display')
        self.assertEqual("Sat, Jul 27", check_out_sel_day.text)

    def test_03_sel_person_num(self):
        # select person num
        person_num_button = self.driver.find_element_by_id('xp__guests__toggle')
        person_num_button.click()

        # click '-' button to set one adults only
        group_adults = self.driver.find_element_by_css_selector('.sb-group__field.sb-group__field-adults')
        adults_button_minus = \
            group_adults.find_element_by_css_selector('.bui-button.bui-button--secondary.bui-stepper__subtract-button')
        adults_button_minus.click()
        time.sleep(1)

        # check if adults num is 1
        adults_num = group_adults.find_element_by_class_name('bui-stepper__display')
        self.assertEqual('1', adults_num.text)

        # set children to 2
        group_children = self.driver.find_element_by_css_selector('.sb-group__field.sb-group-children')
        children_button_add = \
            group_children.find_element_by_css_selector('.bui-button.bui-button--secondary.bui-stepper__add-button')

        children_button_add.click()
        children_button_add.click()
        time.sleep(1)

        # check if children num is 2
        children_num = group_children.find_element_by_class_name('bui-stepper__display')
        self.assertEqual('2', children_num.text)

    def test_04_search_submit(self):
        # find search button
        search_button = self.driver.find_element_by_class_name('sb-searchbox__button')
        search_button.submit()
        time.sleep(2)

        # check title is "Booking.com: Hotels in Auckland. Book your hotel now!"
        self.assertEqual("Booking.com: Hotels in Auckland. Book your hotel now!", self.driver.title)


if __name__ == '__main__':
    unittest.main(verbosity=2)





