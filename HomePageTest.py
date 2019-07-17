import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # Navi to the page
        cls.driver.get('https://www.booking.com/')

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def test_search_by_location(self):
        search_field = self.driver.find_element(By.ID, 'ss')
        # search_field.clear()
        # search_field.send_keys('New Zealand')
        # time.sleep(3)

        # check attribute
        self.assertEqual('Type your destination', search_field.get_attribute('aria-label'))

    def test_search_button_enable(self):
        # get search button
        search_button = self.driver.find_element(By.CLASS_NAME, 'sb-searchbox__button')

        # check search button is enabled
        self.assertTrue(search_button.is_enabled())

    def test_count_of_promo_items(self):
        # get promotion list
        promo_list = self.driver.find_element(By.CLASS_NAME, 'promo-section')

        # get image from promotion list
        promo_items = promo_list.find_elements(By.TAG_NAME, 'img')

        # check there are 2 tags displayed on the page
        self.assertEqual(2, len(promo_items))

    def test_count_of_index_section(self):
        # get index list
        index_list = self.driver.find_element(By.CSS_SELECTOR, '.d-index__section.bui-spacer--large')

        # get image from index list
        index_items = index_list.find_elements(By.TAG_NAME, 'img')

        # check there are 5 tags displayed on the page
        self.assertEqual(5, len(index_items))

        # print 5 cities in total :)
        for item in index_items:
            print(item.get_attribute('alt'))

    def test_select_currency(self):
        # get currency element
        currency_el = self.driver.find_element_by_css_selector('li[data-id=currency_selector]')

        # click to open currency drop-down list
        currency_el.click()

        # empty list for capturing actual options displayed in the dropdown
        act_options = []

        # get the Your language dropdown as instance of Select class
        select_currency = \
            self.driver.find_element_by_id('currency_dropdown_all')
        select_currency_items = \
            select_currency.find_elements_by_tag_name('li')

        print(len(select_currency_items))

        # check number of options in dropdown
        self.assertEqual(50, len(select_currency_items))

        print(select_currency_items[0].text)


        # select US dollar
        currency_us = self.driver.find_element(By.CSS_SELECTOR, '.currency_USD')
        currency_us.click()
        time.sleep(3)

        # check currency is switched to USD
        self.assertTrue('selected_currency=USD' in self.driver.current_url)
        #self.assertEqual('USD', currency_us.get_attribute('data-lang'))




if __name__ == '__main__':
    unittest.main(verbosity=2)
