import unittest
from app import sumar

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativa(self):
        self.assertEqual(sumar(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()
