import unittest
from main import Kalkulacka

class Test_Kalkulacka(unittest.TestCase):

    def test_sum(self):
        calc = Kalkulacka()
        self.assertEqual(calc.sum(), 238)

    def test_mean(self):
        calc = Kalkulacka()
        self.assertAlmostEqual(calc.mean(), 39.67, places=2)

    def test_max(self):
        calc = Kalkulacka()
        self.assertEqual(calc.max(), 122)

    def test_min(self):
        calc = Kalkulacka()
        self.assertEqual(calc.min(), 4)

if __name__ == '__main__':
    unittest.main()