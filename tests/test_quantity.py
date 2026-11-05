import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(parse_quantity("  5 "), 5)

    def test_zero_quantity(self):
        """Zero is a valid quantity (e.g. empty bin)."""
        self.assertEqual(parse_quantity("0"), 0)

    def test_negative_quantity_raises(self):
        """Negative quantities must be rejected with ValueError."""
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        """Arbitrary negative values must also be rejected."""
        with self.assertRaises(ValueError):
            parse_quantity("-100")
