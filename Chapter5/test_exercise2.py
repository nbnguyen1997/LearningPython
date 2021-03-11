import unittest
from Chapter5.exercise2 import check_fermat


class Test_exercise2(unittest.TestCase):
    def test_check_fermat(self):
        self.assertTrue(check_fermat(3, 4, 5, 2))
        self.assertFalse(check_fermat(4, 3, 5, 5))
