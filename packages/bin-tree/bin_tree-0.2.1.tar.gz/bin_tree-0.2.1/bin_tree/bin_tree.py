#  Copyright (c) 2021  SBA - MIT License

from collections import MutableMapping, Mapping, MutableSet


class Node:
    """
    Default node class.

    This class contains what is required to add and remove nodes, as
    well as iterate a subtree, but does not attempt to balance the tree
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    # noinspection PyUnusedLocal
    def adjust(self, child, delta):
        """
        Balance the tree after an insertion or a removal.

        This implementation does nothing: it is intended to be overridden
        in subclasses

        :param child: the child that was updated
        :type child: Node or a subclass of Node
        :param delta: +1, 0 or -1, used by subclasses
        :type delta: integer
        :return: returns the new root of the subtree (self in that
            implementation) and the new delta
        :rtype: Tuple[Node, int]
        """
        return self, delta

    # noinspection PyMethodMayBeStatic
    def side(self):
        """Define the preferred side for searching next node to remove."""
        return -1

    def max_child(self):
        """Search the rightmost child in the subtree"""
        child = self
        while child.right is not None:
            child = child.right
        return child

    def min_child(self):
        """Search the leftmost child in the subtree"""
        child = self
        while child.left is not None:
            child = child.left
        return child

    def rotate_left(self):
        """
        Rotate a subtree to the left.

        :return: the new root of the subtree (the previous right child)
        :rtype: Node
        """
        node = self.right
        self.right = node.left
        node.left = self
        return node

    def rotate_right(self):
        """
        Rotate a subtree to the right.

        :return: the new root of the subtree (the previous left child)
        :rtype: Node
        """
        node = self.left
        self.left = node.right
        node.right = self
        return node

    def __iter__(self):
        if self.left:
            for k in iter(self.left):
                yield k
        yield self
        if self.right:
            for k in iter(self.right):
                yield k


class ValueNode(Node):
    def __init__(self, key, value=None):
        super(ValueNode, self).__init__(key)
        self.value = value


class BinTree:
    """
    Simple implementation of a Binary Tree.

    Keys have to be comparable.This class does not attempt to balance
    its tree. Subclasses are expected to use Node subclasses to provide
    balancing algorithms.
    """

    def __init__(self, node_class=Node):
        self.nodeClass = node_class
        self.root = None
        self._len = 0

    def _insert(self, node: Node, *args):
        """
        Protected method to insert an element into a subtree.

        :param node: root of the subtree
        :type node: node_class
        :param *args: new key or new key value
        :return: the new root of the subtree and an integer helping
            subclasses to re-balance the tree: 0 if subtree should be
            seen as not changed, 1 if an addition has to be considered
        :rtype: Tuple[Node, int]
        """
        key = args[0]
        if node is None:
            self._len += 1
            node, delta = self.nodeClass(*args), 1
        elif key == node.key:
            if issubclass(self.nodeClass, ValueNode):
                node.value = args[1]
            delta = 0
        elif key < node.key:
            node.left, delta = self._insert(node.left, *args)
            node, delta = node.adjust(node.left, delta)
        else:
            node.right, delta = self._insert(node.right, *args)
            node, delta = node.adjust(node.right, delta)
        return node, delta

    def _remove(self, node: Node, key):
        """
        Protected method to remove an element from a subtree.

        :param node: root of the subtree
        :type node: node_class
        :param key: the key to remove
        :type key: a comparable type for the keys
        :return: the new root of the subtree and an integer to help
            subclasses to re-balance the tree: 0 if the tree should be
            seen as not changed, -1 if a deletion should be considered
        :rtype: Tuple[Node, int]
        """
        if node is None:
            raise KeyError()
        if key == node.key:
            if node.left is None:
                self._len -= 1
                return node.right, -1
            elif node.right is None:
                self._len -= 1
                return node.left, -1
            elif node.side() == -1:
                other = node.left.max_child()
                node.key = other.key
                if issubclass(self.nodeClass, ValueNode):
                    node.value = other.value
                node.left, delta = self._remove(node.left, other.key)
                node, delta = node.adjust(node.left, delta)
            else:
                other = node.right.min_child()
                node.key = other.key
                if issubclass(self.nodeClass, ValueNode):
                    node.value = other.value
                node.right, delta = self._remove(node.right, other.key)
                node, delta = node.adjust(node.right, delta)
        elif key < node.key:
            node.left, delta = self._remove(node.left, key)
            node, delta = node.adjust(node.left, delta)
        else:
            node.right, delta = self._remove(node.right, key)
            node, delta = node.adjust(node.right, delta)
        return node, delta

    def _find(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        return self._find(node.left if key < node.key else node.right,
                          key)

    def __len__(self):
        return self._len

    def __iter__(self):
        return (it.key for it in iter(self.root)
                ) if self.root else iter(tuple())

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def height(self):
        """
        Returns the height of the tree.

        :return: height of the tree
        :rtype: int
        """
        return self._height(self.root)

    def dump(self):
        """
        Debugging method that tries to dump a tree.
        """
        msgs = [['' for _ in range(len(self))] for _j in range(self.height())]

        def g(node, level):
            if node.left:
                for kk, ll in g(node.left, level + 1):
                    yield kk, ll
            yield node.key, level
            if node.right:
                for kk, ll in g(node.right, level + 1):
                    yield kk, ll
        for i, (k, l) in enumerate(g(self.root, 0)):
            msgs[l][i] = str(k)
        for lst in msgs:
            print('\t'.join(lst))


class TreeDict(BinTree, MutableMapping):
    """
    Simple MutableMapping implemented as a Binary Tree.

    Keys have to be comparable.This class does not attempt to balance
    its tree. Subclasses are expected to use Node subclasses to provide
    balancing algorithms.
    """

    def __init__(self, items=(), node_class=ValueNode, **kwargs):
        if not issubclass(node_class, ValueNode):
            raise TypeError('node_class must be a subclass of ValueNode')
        super().__init__(node_class)
        if isinstance(items, Mapping):
            for k, v in items.items():
                self.root, _ = self._insert(self.root, k, v)
        for it in items:
            self.root, _ = self._insert(self.root, *it)
        for k, v in kwargs:
            self.root, _ = self._insert(self.root, k, v)

    def __delitem__(self, key) -> None:
        self.root, _ = self._remove(self.root, key)

    def __getitem__(self, key):
        node = self._find(self.root, key)
        if node is None:
            raise KeyError
        return node.value

    def __setitem__(self, k, v) -> None:
        self._insert(self.root, k, v)


class TreeSet(BinTree, MutableSet):
    """
    Simple MutableSet implemented as a binary tree.

    Keys have to be comparable.This class does not attempt to balance
    its tree. Subclasses are expected to use Node subclasses to provide
    balancing algorithms.
    """
    def __init__(self, items=tuple(), node_class=Node):
        super(TreeSet, self).__init__(node_class)
        for it in items:
            self.root, _ = self._insert(self.root, it)

    def add(self, key):
        """
        Inserts a new element in the tree

        :param key: new key
        :type key: a comparable type
        :return: None
        :rtype: NoneType
        """
        self.root, _ = self._insert(self.root, key)

    def discard(self, key) -> None:
        self.root, _ = self._remove(self.root, key)

    def __contains__(self, x) -> bool:
        return self._find(self.root, x) is not None
