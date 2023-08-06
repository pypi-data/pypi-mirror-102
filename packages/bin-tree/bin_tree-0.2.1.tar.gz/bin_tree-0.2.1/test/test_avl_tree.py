#  Copyright (c) 2021  SBA - MIT License

import unittest
from bin_tree.avl_tree import AVLNode, TreeSet, TreeDict
import itertools


class RotateLeft(unittest.TestCase):
    def test_simple(self):
        node = AVLNode(1)
        node.weight = 2
        node.right = AVLNode(2)
        node.right.weight = 1
        node.right.right = AVLNode(3)
        new = node.rotate_left()
        self.assertEqual(2, new.key)
        self.assertEqual(0, new.weight)
        self.assertEqual(0, node.weight)

    def test_normal(self):
        node = AVLNode(2)
        node.weight = 1
        node.left = AVLNode(1)
        node.right = AVLNode(4)
        node.right.left = AVLNode(3)
        node.right.right = AVLNode(5)
        new = node.rotate_left()
        self.assertEqual(4, new.key)
        self.assertEqual(node, new.left)
        self.assertEqual(-1, new.weight)
        self.assertEqual(0, node.weight)

    def test_right(self):
        node = AVLNode(2)
        node.left = AVLNode(1)
        node.weight = 1
        node.right = AVLNode(3)
        node.right.weight = 1
        node.right.right = AVLNode(4)
        new = node.rotate_left()
        self.assertEqual(3, new.key)
        self.assertEqual(node, new.left)
        self.assertEqual(None, node.right)
        self.assertEqual(-1, node.weight)
        self.assertEqual(-1, new.weight)

    def test_left(self):
        node = AVLNode(2)
        node.left = AVLNode(1)
        node.weight = 1
        node.right = AVLNode(4)
        node.right.weight = -1
        node.right.left = AVLNode(3)
        new = node.rotate_left()
        self.assertEqual(4, new.key)
        self.assertEqual(node, new.left)
        self.assertEqual(0, node.weight)
        self.assertEqual(-2, new.weight)


class RotateRight(unittest.TestCase):
    def test_simple(self):
        node = AVLNode(3)
        node.weight = -2
        node.left = AVLNode(2)
        node.left.weight = -1
        node.left.left = AVLNode(1)
        new = node.rotate_right()
        self.assertEqual(2, new.key)
        self.assertEqual(0, new.weight)
        self.assertEqual(0, node.weight)

    def test_normal(self):
        node = AVLNode(4)
        node.weight = -1
        node.left = AVLNode(2)
        node.right = AVLNode(5)
        node.left.left = AVLNode(1)
        node.left.right = AVLNode(3)
        new = node.rotate_right()
        self.assertEqual(2, new.key)
        self.assertEqual(node, new.right)
        self.assertEqual(1, new.weight)
        self.assertEqual(0, node.weight)

    def test_right(self):
        node = AVLNode(3)
        node.left = AVLNode(1)
        node.weight = -1
        node.right = AVLNode(4)
        node.left.weight = 1
        node.left.right = AVLNode(2)
        new = node.rotate_right()
        self.assertEqual(1, new.key)
        self.assertEqual(node, new.right)
        self.assertEqual(None, new.left)
        self.assertEqual(0, node.weight)
        self.assertEqual(2, new.weight)

    def test_left(self):
        node = AVLNode(3)
        node.left = AVLNode(2)
        node.weight = -1
        node.right = AVLNode(4)
        node.left.weight = -1
        node.left.left = AVLNode(1)
        new = node.rotate_right()
        self.assertEqual(2, new.key)
        self.assertEqual(node, new.right)
        self.assertEqual(1, node.weight)
        self.assertEqual(1, new.weight)


class Inserts(unittest.TestCase):
    def test_3(self):
        for i in itertools.permutations(range(1, 4)):
            tree = TreeSet(i)
            self.assertEqual(2, tree.root.key)
            self.assertEqual(0, tree.root.weight)
            self.assertEqual(2, tree.height())
            self.assertEqual((1, 2, 3), tuple(tree))

    def test_7(self):
        for i in itertools.permutations(range(1, 8)):
            tree = TreeSet(i)
            if 3 == tree.height():
                self.assertEqual(4, tree.root.key)
                self.assertEqual(0, tree.root.weight)
                self.assertEqual((1, 2, 3, 4, 5, 6, 7), tuple(tree))


class Delete(unittest.TestCase):
    def test_low_left(self):
        tree = TreeSet((4, 3, 5, 1, 2))
        tree.discard(1)
        self.assertEqual(-1, tree.root.weight)
        self.assertEqual(2, tree.root.left.key)
        self.assertEqual(1, tree.root.left.weight)

    def test_low_right(self):
        tree = TreeSet((4, 3, 5, 1, 2))
        tree.discard(3)
        self.assertEqual(-1, tree.root.weight)
        self.assertEqual(2, tree.root.left.key)
        self.assertEqual(-1, tree.root.left.weight)

    def test_top_left(self):
        tree = TreeSet((3, 4, 2, 1))
        tree.discard(3)
        self.assertEqual(2, tree.root.key)
        self.assertEqual(0, tree.root.weight)
        self.assertEqual(2, tree.height())

    def test_top_right(self):
        tree = TreeSet((2, 1, 4, 3))
        tree.discard(2)
        self.assertEqual(3, tree.root.key)
        self.assertEqual(0, tree.root.weight)
        self.assertEqual(2, tree.height())

    def test_rotate_left(self):
        tree = TreeSet((3, 2, 5, 1, 4, 6, 7))
        self.assertEqual(1, tree.root.weight)
        tree.discard(1)
        self.assertEqual(5, tree.root.key)
        self.assertEqual(0, tree.root.weight)

    def test_rotate_right(self):
        tree = TreeSet((5, 3, 6, 2, 4, 7, 1))
        self.assertEqual(-1, tree.root.weight)
        tree.discard(6)
        self.assertEqual(3, tree.root.key)
        self.assertEqual(0, tree.root.weight)


if __name__ == '__main__':
    unittest.main()
