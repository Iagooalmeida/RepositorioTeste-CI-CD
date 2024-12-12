import unittest
from calcula_imc import calculate_bmi

class TestIMC(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(50, 1.60), 19.53, places=2)
        self.assertAlmostEqual(calculate_bmi(80, 1.80), 24.69, places=2)
        self.assertEqual(calculate_bmi(70, 0), "Height must be greater than zero")  # Test for height zero

if __name__ == "__main__":
    unittest.main()