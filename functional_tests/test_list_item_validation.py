import time

from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        #John goes to the home page and tries to submit an empty list
        #item. He hits enter on an empty input box.

        #The home page refreshes and there is an error message saying
        #that list items cannot be blank

        #He tries again with some text for the item, which works

        #He then decides to try submitting another blank item

        #He recieves another warning on the list page

        #He can make it go away by filling some text in

        self.fail('write me!')



