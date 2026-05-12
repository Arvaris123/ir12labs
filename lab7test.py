import os
import tempfile
import unittest

from lab7 import min_cable_length, solve


class TestLab7(unittest.TestCase):
    def test_two_islands(self):
        self.assertEqual(min_cable_length([[0, 5], [5, 0]]), 5)

    def test_four_islands(self):
        matrix = [
            [0, 2, 3, 4],
            [2, 0, 5, 6],
            [3, 5, 0, 1],
            [4, 6, 1, 0],
        ]
        self.assertEqual(min_cable_length(matrix), 6)

    def test_solve_from_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "islands.csv")
            with open(path, "w", encoding="utf-8") as f:
                f.write("0,1,3\n1,0,2\n3,2,0\n")
            self.assertEqual(solve(path), 3)


if __name__ == "__main__":
    unittest.main()
