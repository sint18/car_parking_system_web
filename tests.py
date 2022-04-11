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
        self.assertEqual(format_currency(1000), "1,000", "Should be 1,000")
        self.assertEqual(format_currency(10000), "10,000", "Should be 10,000")
        self.assertEqual(format_currency(100000),
                         "100,000", "Should be 100,000")
        self.assertEqual(format_currency(100), "100", "Should be 100")


if __name__ == "__main__":
    unittest.main()
