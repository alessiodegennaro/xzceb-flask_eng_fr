import unittest

class Testing(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        #self.assertEqual(englishToFrench(" "), " ")

    def test_f2e(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        #self.assertEqual(frenchToEnglish(" "), " ")