import unittest
from functions import format_currency, calculate_fees


class TestFunctions(unittest.TestCase):
    def test_calculate_fees(self):
        self.assertEqual(calculate_fees(
            2, 500, 200), 700, "Should be 700")
        self.assertEqual(calculate_fees(
            1, 500, 200), 500, "Should be 500")
        self.assertEqual(calculate_fees(
            3, 500, 200), 900, "Should be 900")

    def test_format_currency(self):
        self.assertEqual(format_currency(1000), "1,000 MMK", "Should be 1,000")
        self.assertEqual(format_currency(10000),
                         "10,000 MMK", "Should be 10,000")
        self.assertEqual(format_currency(100000),
                         "100,000 MMK", "Should be 100,000")
        self.assertEqual(format_currency(100), "100 MMK", "Should be 100")

    def test_currency(self):
        self.assertEqual(int("100,000 MMK"), "100000", "Should be 100000")


if __name__ == "__main__":
    unittest.main()
