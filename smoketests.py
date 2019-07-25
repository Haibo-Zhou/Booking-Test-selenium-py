import unittest
from xmlrunner import xmlrunner
from HomePageTest import HomePageTest
from SearchHotel import SearchHotel


# get all test from HomePageTest and SearchHotel class
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchHotel)

# create a test suite combining search_tests and home_page_tests
smoke_tests = unittest.TestSuite([home_page_tests, search_tests])


# run the suite
xmlrunner.XMLTestRunner(verbosity=2, output='test-report').run(smoke_tests)