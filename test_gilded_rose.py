# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("food", 0, 0),Item("pinapple", 10, 40),Item("Aged Brie", 11, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        #self.assertEqual("foo", items[0].name)

if __name__ == '__main__':
    unittest.main()
