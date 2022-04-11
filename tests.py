import unittest
import functions


class TestFunctions(unittest.TestCase):
    def test_calculate_fees(self):
        self.assertEqual(functions.calculate_fees(
            2, 500, 200), 700, "Should be 700")
        self.assertEqual(functions.calculate_fees(
            1, 500, 200), 500, "Should be 500")
        self.assertEqual(functions.calculate_fees(
            3, 500, 200), 900, "Should be 900")


if __name__ == "__main__":
    unittest.main()
