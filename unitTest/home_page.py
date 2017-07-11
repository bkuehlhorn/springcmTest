import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from hamcrest import *


class HomePage(unittest.TestCase):

    def setUp(self):
        '''
        Create webdriver for testing. Chrome is used for initial test development and working test failures
        Headless browser should be used for normal testing when possible. Headless browser may not support all tests.

        Chrome Headless browser should be replace Polterghist headless browser.

        :return:
        '''
        layouts = [[1260, 740], # desktop
                   #todo: add more layouts for tablet and phone
                  ]
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(*layouts[0])
        self.driver.get("http://www.springcm.com")

    def test_rendered(self):
        '''
        Verify home page is rendered. Business team identifies key information to validate.

        :return:
        '''
        driver = self.driver

        assert u'SpringCM | Optimize Your Contract and Document Process' in driver.title
        assert u'springcm.com' in driver.find_element_by_class_name('widget-span').find_element_by_tag_name('a').get_attribute('href')
        # get from business team additioal components to validate

    def test_search_field(self):
        '''
        Verify Search Field is visible

        :return:
        '''
        driver = self.driver
        # need more research to do without Javascript
        driver.execute_script("document.getElementsByClassName('fa-search')[01].click()")
        assert_that(driver.find_element_by_id('___gcse_1').is_displayed(), is_(True))
        # xx = driver.find_element_by_class_name('gsc-input')

    def test_search_contract_management(self):
        '''
        Search for 'Contract Management' and verify proper results.

        :return:
        '''
        driver = self.driver
        driver.execute_script("document.getElementsByClassName('fa-search')[01].click()")
        driver.find_element_by_id('gsc-i-id2').send_keys('Contract Management')
        driver.find_element_by_id('gsc-i-id2').send_keys(Keys.ENTER)

        assert_that(driver.find_element_by_tag_name('h1').text, equal_to('Search Results'))
        # Add additional validation required by Business Teams.


    def tearDown(self):
        '''
        Close browser
        Do any other cleanup necessary

        :return:
        '''
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
