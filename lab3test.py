import unittest
from lab3func import (
    Node,
    find_successor,
    build_custom_tree,
    inorder_invert,
    write_tree,
    read_tree,
    display_upside_down,
    FILE_PATH,
)


class TestBinaryTreeSuccessor(unittest.TestCase):
    def setUp(self):
        self.root = Node(10)
        self.n5 = Node(5, parent=self.root)
        self.n15 = Node(15, parent=self.root)
        self.root.left = self.n5
        self.root.right = self.n15

        self.n7 = Node(7, parent=self.n5)
        self.n5.right = self.n7

        self.n20 = Node(20, parent=self.n15)
        self.n15.right = self.n20
        self.n12 = Node(12, parent=self.n20)
        self.n20.left = self.n12

    def test_successor_up(self):
        res = find_successor(self.root, self.n7)
        self.assertEqual(res.value, 10)

    def test_successor_down(self):
        res = find_successor(self.root, self.n15)
        self.assertEqual(res.value, 12)


def main():
    tree = build_custom_tree()
    write_tree(tree)
    _, reconstructed = read_tree()
    display_upside_down(reconstructed)


if __name__ == "__main__":
    main()
    print("\n=== Тести ===")
    unittest.main(exit=False)
