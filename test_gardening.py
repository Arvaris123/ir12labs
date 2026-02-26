import unittest
from gardening import task_func

class TestGardening(unittest.TestCase):
    
    def test_m4_n5(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        expected_route = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16]
        res, _, _, _ = task_func(matrix)
        self.assertEqual(res, expected_route)

    def test_n1_m6(self):
        matrix = [[1], [2], [3], [4], [5], [6]]
        res, _, _, _ = task_func(matrix)
        self.assertEqual(res, [1, 2, 3, 4, 5, 6])

    def test_m2_n4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        res, _, _, _ = task_func(matrix)
        self.assertEqual(res, [1, 2, 3, 4, 8, 7, 6, 5])

    def test_example_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        res, stops_cnt, history, final_sum = task_func(matrix)
        
        expected_route = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13]
        self.assertEqual(res, expected_route)
        self.assertEqual(len(res), 16)
        self.assertEqual(final_sum, 136)

if __name__ == '__main__':
    unittest.main()
