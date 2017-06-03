from django.test import TestCase

from lists.forms import (ItemForm, EMPTY_ITEM_ERROR,
                         ExistingListItemForm, DUPLICATE_ITEM_ERROR)
from lists.models import Item, List

class ItemFormTestCase(TestCase):
    def test_form_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'i am an item'})
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'i am an item')
        self.assertEqual(new_item.list, list_)


class ExistingListItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        todo_list = List.objects.create()
        form = ExistingListItemForm(for_list=todo_list, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_validation_for_duplicate_items(self):
        todo_list = List.objects.create()
        Item.objects.create(list=todo_list, text='there can only be one')
        form = ExistingListItemForm(for_list=todo_list,
                                    data={'text': 'there can only be one'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])

    def test_form_save(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': 'henlo'})
        new_item = form.save()
        self.assertEqual(new_item, Item.objects.first())
