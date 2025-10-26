def calc_discount(level, amount):
    if level == 'basic':
        return amount * 0.95
    elif level == 'silver':
        return amount * 0.90
    elif level == 'gold':
        return amount * 0.85
    else:
        raise ValueError('unknown level')

import unittest
class TestCalulateDiscount(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(calc_discount('basic', 100), 95.0)

    def test_silver(self):
        self.assertEqual(calc_discount('basic', 100), 90.0)

    def test_gold(self):
        self.assertEqual(calc_discount('basic', 100), 85.0)

def test_invalid(self):
    with self.assertRaises(ValueError):
        calc_discount('platinum', 100)

if __name__ == '__main__':
    unittest.main()


