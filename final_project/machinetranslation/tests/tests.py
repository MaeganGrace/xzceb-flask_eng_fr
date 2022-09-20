import unittest

from translator import french_to_english, english_to_french

class TestFrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('None'), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

class TestEnglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('None'), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

unittest.main()