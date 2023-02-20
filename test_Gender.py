from unittest import TestCase

from Gender import convert_gender


class Test(TestCase):
    def test_convert_gender_when_male(self):
        actual = convert_gender("M")
        expected = "Male"
        self.assertEqual(actual, expected)


class Test(TestCase):
    def test_convert_gender_when_female(self):
        actual = convert_gender("F")
        expected = "female"
        self.assertEqual(actual, expected)

class Test(TestCase):
    def test_convert_gender_when_unkown(self):
        actual = convert_gender("hello")
        expected = "Unkown gender"
        self.assertEqual(actual, expected)
