import unittest
from Chapter6.exercise4 import is_power


class Test_exercise4(unittest.TestCase):
    def test_is_power(self):
        self.assertTrue(is_power(9, 3))
        self.assertTrue(is_power(16, 4))
        self.assertFalse(is_power(10, 5))
        self.assertFalse(is_power(3, 9))


if __name__ == "__main__":
    unittest.main()
