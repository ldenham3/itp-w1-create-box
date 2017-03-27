import unittest

from create_box import *

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

first_hollow_expected = """
****
*  *
****
""".lstrip()

second_hollow_expected = """
@""".lstrip()

third_hollow_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
x                      x
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_large_box(self):
        self.assertEqual(create_box(3,24,'x'), third_box_expected)
        
    def test_hollow_box(self):
        self.assertEqual(create_hollow(3, 4, '*'), first_hollow_expected)

    def test_small_hollow_box(self):
        self.assertEqual(create_hollow(1, 1, '@'), second_hollow_expected)
        
    def test_large_hollow_box(self):
        self.assertEqual(create_hollow(3,24,'x'), third_hollow_expected)
