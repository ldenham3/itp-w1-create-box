import unittest

from create_box import create_box

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

#make tests cases
first_hollow_box_expected = ""
second_hollow_box_expected = ""
third_hollow_box_expected = ""


class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)
        
    def test_large_box(self):
        self.assertEqual(create_box(3,24,'x'), third_box_expected)

class TestCreateHollowBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_hollow_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_hollow_box_expected)
        
    def test_large_box(self):
        self.assertEqual(create_box(3,24,'x'), third_hollow_box_expected)