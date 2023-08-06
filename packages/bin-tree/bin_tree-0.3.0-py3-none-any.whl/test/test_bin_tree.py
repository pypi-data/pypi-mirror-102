import unittest
import bin_tree


class TestBTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = bin_tree.BinTree((4, 2, 1, 3, 6, 5, 7))

    def test_len(self):
        self.assertEqual(7, len(self.tree))
        self.assertTrue(3, self.tree.height())

    def test_del_leaf(self):
        del self.tree[3]
        self.assertEqual(6, len(self.tree))
        self.assertEqual(3, self.tree.height())

    def test_del_root(self):
        del self.tree[4]
        self.assertEqual(6, len(self.tree))
        self.assertEqual(3, self.tree.height())
        self.assertEqual(3, self.tree.root.key)

    def test_half_tree(self):
        for i in (1, 2, 3, 4):
            del self.tree[i]
        self.assertEqual(3, len(self.tree))
        self.assertTrue(2, self.tree.height())
        self.assertEqual(6, self.tree.root.key)

    def test_all_leaves(self):
        for i in (1, 3, 5, 7):
            del self.tree[i]
        self.assertEqual(3, len(self.tree))
        self.assertTrue(2, self.tree.height())
        self.assertEqual(4, self.tree.root.key)

    def test_left(self):
        self.tree.root = self.tree.root.rotate_left()
        self.assertEqual(7, len(self.tree))
        self.assertEqual(4, self.tree.height())
        self.assertEqual(6, self.tree.root.key)
        self.assertEqual(list(range(1, 8)), list(self.tree))

    def test_right(self):
        self.tree.root = self.tree.root.rotate_right()
        self.assertEqual(7, len(self.tree))
        self.assertEqual(4, self.tree.height())
        self.assertEqual(2, self.tree.root.key)
        self.assertEqual(list(range(1, 8)), list(self.tree))


if __name__ == '__main__':
    unittest.main()
