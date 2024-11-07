import unittest
from app import calculate

class TestApp(unittest.TestCase):
    def test_calculate(self):
        result1, result2 = calculate(5, 3, 2)
        self.assertEqual(result1, 6)  # Kiểm tra a + b - c
        self.assertEqual(result2, 7.5)  # Kiểm tra a * b / c

if __name__ == "__main__":
    unittest.main()
