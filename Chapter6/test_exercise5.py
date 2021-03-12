import unittest
from Chapter6.exercise5 import gcd


class TestExercise5(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(12, 3), 3)
        self.assertEqual(gcd(36, 16), 4)
        self.assertEqual(gcd(-36, 12), 12)
        self.assertNotEqual(gcd(-12, 3), 4)
        self.assertNotEqual(gcd(15, 2), 4)


if __name__ == "__main__":
    unittest.main()
