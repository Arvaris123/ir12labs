import unittest

from lab9 import find_all


class TestLab9(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_all("abracadabra", "abr"), [0, 7])

    def test_overlap(self):
        self.assertEqual(find_all("aaaa", "aa"), [0, 1, 2])

    def test_not_found(self):
        self.assertEqual(find_all("hello", "xyz"), [])


if __name__ == "__main__":
    unittest.main()
