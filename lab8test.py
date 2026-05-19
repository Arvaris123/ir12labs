import unittest

from lab8 import count_paths


class TestLab8(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(count_paths(["aaa", "cab", "def"]), 5)

    def test_example2(self):
        self.assertEqual(count_paths(["abcdefaghi"]), 2)

    def test_example3(self):
        self.assertEqual(count_paths(["aaaaaaa"] * 6), 201684)


if __name__ == "__main__":
    unittest.main()
