import unittest
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Yes'), 'Oui')
        self.assertEqual(englishToFrench('Love'), 'Amour')
        self.assertEqual(englishToFrench('Thanks'), 'Merci')
        self.assertEqual(englishToFrench('Smile'), 'Sourire')
        
    def test2(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench(' '), ' ')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Oui'), 'Yes')
        self.assertEqual(frenchToEnglish('Amour'), 'Love')
        self.assertEqual(frenchToEnglish('Sourire'), 'Smile')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
    
    def test2(self):
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(frenchToEnglish(' '), ' ')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
