import unittest
from bin_tree.red_black_tree import TreeSet, TreeDict, Color


class Insert(unittest.TestCase):
    def test_simple(self):
        tree = TreeSet((2, 1, 3))
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(2, tree.height())
        self.assertEqual(1, tree.black_height())

    def test_swap(self):
        tree = TreeSet((2, 1, 3))
        tree.add(4)
        self.assertEqual(Color.BLACK, tree.root.color)
        self.assertEqual(Color.BLACK, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(Color.RED, tree.root.right.right.color)

    def test_left(self):
        tree = TreeSet((2, 1, 3, 4))
        tree.add(5)
        self.assertEqual(4, tree.root.right.key)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(list(range(1, 6)), list(tree))

    def test_right(self):
        tree = TreeSet((4, 3, 5, 2))
        tree.add(1)
        self.assertEqual(2, tree.root.left.key)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.right.color)
        self.assertEqual(list(range(1, 6)), list(tree))

    def test_double_left(self):
        tree = TreeSet((2, 1, 3, 5))
        tree.add(4)
        self.assertEqual(4, tree.root.right.key)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(list(range(1, 6)), list(tree))


class Delete(unittest.TestCase):
    def test_red_single(self):
        tree = TreeSet((2, 1, 5, 3))
        tree.discard(3)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(2, tree.height())
        self.assertEqual((1, 2, 5), tuple(tree))

    def test_root_right(self):
        tree = TreeSet((2, 1, 4, 3, 5, 6))
        self.assertEqual(2, tree.black_height())
        self.assertEqual(4, tree.height())
        tree.discard(2)
        self.assertEqual(3, tree.root.key)
        self.assertEqual(5, tree.root.right.key)
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)

    def test_root_left(self):
        tree = TreeSet((5, 3, 6, 1, 4, 2))
        self.assertEqual(2, tree.black_height())
        self.assertEqual(4, tree.height())
        tree.discard(5)
        self.assertEqual(4, tree.root.key)
        self.assertEqual(2, tree.root.left.key)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.left.color)
        self.assertEqual(Color.BLACK, tree.root.left.right.color)

    def test_black_one_red_child(self):
        tree = TreeSet((4, 2, 6, 1, 3, 5, 8, 7))
        self.assertEqual(2, tree.black_height())
        tree.discard(8)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)

    def test_red_parent(self):
        tree = TreeSet((4, 2, 8, 1, 3, 6, 10, 5, 7, 9))
        self.assertEqual(2, tree.black_height())
        tree.discard(9)
        tree.discard(10)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(Color.RED, tree.root.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(Color.RED, tree.root.right.right.left.color)

    def test_all_black(self):
        tree = TreeSet((1, 2, 3, 4, 5, 6, 7))
        self.assertEqual(3, tree.black_height())
        self.assertEqual(3, tree.height())
        tree.discard(7)
        self.assertEqual(2, tree.black_height())
        self.assertEqual(4, tree.root.key)
        self.assertEqual(Color.RED, tree.root.left.color)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(Color.RED, tree.root.right.left.color)
        self.assertEqual(None, tree.root.right.right)

    def test_black_sibling_red_child(self):
        tree = TreeSet((1, 2, 3, 4, 6, 8, 9))
        self.assertEqual(3, tree.black_height())
        self.assertEqual(3, tree.height())
        tree.add(5)
        tree.add(7)
        self.assertEqual(3, tree.black_height())
        self.assertEqual(4, tree.height())
        tree.discard(9)
        self.assertEqual(3, tree.black_height())
        self.assertEqual(4, tree.height())
        self.assertEqual(4, tree.root.key)
        self.assertEqual(6, tree.root.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(5, tree.root.right.left.key)
        self.assertEqual(Color.BLACK, tree.root.right.left.color)
        self.assertEqual(8, tree.root.right.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.right.color)
        self.assertEqual(7, tree.root.right.right.left.key)
        self.assertEqual(Color.RED, tree.root.right.right.left.color)

    def test_red_sibling(self):
        tree = TreeSet((1, 2, 3, 4, 6, 9, 10, 5, 7, 8))
        self.assertEqual(3, tree.black_height())
        tree.discard(10)
        self.assertEqual(6, tree.root.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.color)
        self.assertEqual(8, tree.root.right.right.key)
        self.assertEqual(Color.RED, tree.root.right.right.color)
        self.assertEqual(7, tree.root.right.right.left.key)
        self.assertEqual(Color.BLACK, tree.root.right.right.left.color)
        self.assertEqual(9, tree.root.right.right.right.key)
        self.assertEqual(Color.BLACK, tree.root.right.right.right.color)


class TestDictTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = TreeDict((i, 2 * i) for i in range(1, 8))

    def test_init(self):
        self.assertEqual(3, self.tree.black_height())
        self.assertEqual(3, self.tree.height())
        self.assertEqual(4, self.tree.root.key)

    def test_get(self):
        self.assertEqual(12, self.tree[6])

    def test_set(self):
        self.tree[6] = 18
        self.assertEqual(18, self.tree[6])

    def test_del(self):
        del self.tree[4]
        self.assertEqual(2, self.tree.black_height())
        self.assertEqual(3, self.tree.height())
        self.assertEqual(3, self.tree.root.key)


if __name__ == '__main__':
    unittest.main()
