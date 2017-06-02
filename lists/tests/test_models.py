from django.test import TestCase
from django.core.exceptions import ValidationError

from lists.models import Item, List



class ItemModelTest(TestCase):

    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='platypus')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='platypus')
            item.full_clean()

    def test_can_save_same_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='echidna')
        duplicate_item = Item(list=list2, text='echidna')
        try:
            duplicate_item.full_clean()
        except ValidationError as test_failed:
            print("Duplicate items should be able to exist in different"
                  " lists")
            raise

    def test_list_ordering(self):
        list1 = List.objects.create()
        expected_item_order = []
        for item_number in range(3):
            expected_item_order.append(
                Item.objects.create(list=list1,
                    text='item-{}'.format(item_number))
            )
        self.assertListEqual(list(Item.objects.all()), expected_item_order)

    def test_string_representation(self):
        item = Item(text='henlo i am an item')
        self.assertEqual(str(item), item.text)


class ListModelTest(TestCase):

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(),
                        '/lists/{}/'.format(list_.id))
