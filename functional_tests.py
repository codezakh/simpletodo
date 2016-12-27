from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])



    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about an online to-do app. She goes 
        #to check out its homepage.
        self.browser.get('http://localhost:8000')

        #she notices the page title and header mention todo lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        #she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        #she types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        #when she hits enter, the page updates, and now the
        #page lists "1: Buy peacock feathers" as an item in the
        #to-do list table
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        #there is still a text box inviting her to add another item
        #she enters "Use peacock feathers to make a fly".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')

        #the page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        #Edith wonders whether the site will remember her list. Then she
        #sees that the site has generated a unique url for her -- there is
        #some explanatory text to that effect.
        self.fail('Finish the test!')


if __name__== '__main__':
    unittest.main(warnings='ignore')

