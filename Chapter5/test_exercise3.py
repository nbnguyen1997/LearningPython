import unittest
from Chapter5.exercise3 import is_triangle


class Test_exercise3(unittest.TestCase):
    def test_is_triangle(self):
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertFalse(is_triangle(1, 1, -4))


if __name__ == "__main__":
    unittest.main()
