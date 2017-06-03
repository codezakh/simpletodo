import time
from unittest import skip

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condition

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def get_error_element(self):
        error = self.browser.find_element_by_css_selector('.has-error')
        return error

    def test_cannot_add_empty_list_items(self):
        flashed_error_message = (By.CSS_SELECTOR, '.has-error')
        table_rendered = (By.ID, 'id_list_table')

        #John goes to the home page and tries to submit an empty list
        #item. He hits enter on an empty input box.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        #The home page refreshes and there is an error message saying
        #that list items cannot be blank
        error = WebDriverWait(self.browser, 3).until(
                condition.presence_of_element_located(flashed_error_message))
        #error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #He tries again with some text for the item, which works
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        #He then decides to try submitting another blank item
        self.get_item_input_box().send_keys(Keys.ENTER)

        #He recieves another warning on the list page
        WebDriverWait(self.browser,3).until(
                condition.presence_of_element_located(table_rendered))
        self.check_for_row_in_list_table('1: Buy milk')
        error = WebDriverWait(self.browser, 3).until(
                condition.presence_of_element_located(flashed_error_message))
        self.assertEqual(error.text, "You can't have an empty list item")

        #He can make it go away by filling some text in
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.RETURN)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Throckmorton goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy sprongles\n')
        self.check_for_row_in_list_table('1: Buy sprongles')

        # It accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy sprongles\n')

        # It sees an error message
        self.check_for_row_in_list_table('1: Buy sprongles')
        error = self.get_error_element()
        self.assertIn("You've already got this in your list",
                    error.text)

    def test_error_messages_are_cleared_on_input(self):
        # Otto von Bismarck starts a new list with a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # He starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('meep')

        # He sees the error message has disappeared!
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
