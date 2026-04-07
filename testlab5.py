import unittest
from lab5 import flood_fill


class TestFloodFill(unittest.TestCase):

    def test_example_from_task(self):
        matrix = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        flood_fill(matrix, 3, 9, 'C')
        expected = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'G', 'C'],
            ['W', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C'],
            ['W', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'B', 'B', 'B', 'C', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
        ]
        self.assertEqual(matrix, expected)


if __name__ == '__main__':
    unittest.main()
