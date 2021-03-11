import unittest
from Chapter6.Exercise2 import ack


class Test_exercise2(unittest.TestCase):
    def test_ack(self):
        self.assertEqual(ack(3, 4), 125)
        self.assertEqual(ack(3, 3), 61)
        self.assertEqual(ack(2, 4), 11)


if __name__ == "__main__":
    unittest.main()
