import unittest
from lab4 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    
    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_add_and_remove(self):
        self.pq.add("Task 2", 2)
        self.pq.add("Task 7", 7)
        self.pq.add("Task 8", 8)
        self.pq.add("Task 4", 4)
        self.pq.add("Task 10", 10)

        self.assertEqual(self.pq.remove(), ("Task 10", 10))
        self.assertEqual(self.pq.remove(), ("Task 8", 8))
        self.assertEqual(self.pq.remove(), ("Task 7", 7))
        self.assertEqual(self.pq.remove(), ("Task 4", 4))
        self.assertEqual(self.pq.remove(), ("Task 2", 2))
        self.assertIsNone(self.pq.remove())

    def test_peek(self):
        self.assertIsNone(self.pq.peek())
        
        self.pq.add("Low Priority", 10)
        self.pq.add("High Priority", 100)
        self.assertEqual(self.pq.peek(), ("High Priority", 100))
        self.assertEqual(self.pq.remove(), ("High Priority", 100))
        self.assertEqual(self.pq.peek(), ("Low Priority", 10))

    def test_empty_queue(self):
        self.assertIsNone(self.pq.remove())
        self.assertIsNone(self.pq.peek())

    def test_equal_priorities(self):
        self.pq.add("Task A", 5)
        self.pq.add("Task B", 5)
        self.pq.add("Task C", 5)
        
        extracted = []
        for _ in range(3):
            extracted.append(self.pq.remove())
            
        self.assertEqual(len(extracted), 3)
        for task in extracted:
            self.assertEqual(task[1], 5)
            self.assertIn(task[0], ["Task A", "Task B", "Task C"])
            
        self.assertIsNone(self.pq.remove())

if __name__ == "__main__":
    unittest.main()
