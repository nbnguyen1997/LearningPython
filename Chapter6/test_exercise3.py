import unittest
from Chapter6.exercise3 import is_palindrome


class Test_exercise3(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("redivider"))
        self.assertFalse(is_palindrome("Nguyen"))


if __name__ == "__main__":
    unittest.main()
