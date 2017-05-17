import time

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        #Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        #she notices the input box is centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=5)

        #she starts a new list and sees that the input is
        #centered there as well
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512, 
                delta=5)
