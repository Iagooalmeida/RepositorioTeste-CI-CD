
import unittest
from imc_calculadora import calcula_imc

class TestIMC(unittest.TestCase):

    def test_calcula_imc(self):
        self.assertAlmostEqual(calcula_imc(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(calcula_imc(50, 1.60), 19.53, places=2)
        self.assertAlmostEqual(calcula_imc(80, 1.80), 24.69, places=2)
        with self.assertRaises(ValueError):
            calcula_imc(70, 0)  # Teste para altura zero

if __name__ == "__main__":
    unittest.main()
