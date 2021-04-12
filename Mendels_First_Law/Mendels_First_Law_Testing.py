import unittest
from Mendels_First_Law import dominant_prob

class Testdominantprob(unittest.TestCase):
    def test_only_dominant(self):
        self.assertEqual(dominant_prob(5, 0, 0), 1)
    
    def test_only_recessive(self):
        self.assertEqual(dominant_prob(0, 0, 5), 0)
        
    def test_only_heterozygous(self):
        self.assertEqual(dominant_prob(0, 5, 0), 0.75)
        
    def test_mixed(self):
        self.assertEqual(dominant_prob(1,1,1), 5/6)
        
        
if __name__ == '__main__':
    unittest.main()