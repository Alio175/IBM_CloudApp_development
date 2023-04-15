import unittest
from translator import englishToFrench, frenchToEnglish

class TestMyModule(unittest.TestCase):
    
    def test_enlishToFrench(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    
    def test_frrenchToEglish(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        
        
        
if __name__ == '__main__ ':
    unittest.main()