#  Copyright (c) 2021  SBA - MIT License

from collections import MutableMapping, Mapping, MutableSet
from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar, Tuple, Optional, cast
# Python<3.8 has no support for Protocol: hack to avoid the error
try:
    from typing import Protocol
except ImportError:
    Protocol = object


class Comparable(Protocol, metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...


CT = TypeVar('CT', bound=Comparable)


class Node:
    """
    Default node class.

    This class contains what is required to add and remove nodes, as
    well as iterate a subtree, but does not attempt to balance the tree
    """
    def __init__(self, key: CT):
        self.key = key
        self.child = [cast('Node', None), cast('Node', None)]

    @property
    def left(self) -> 'Node':
        return self.child[0]

    @left.setter
    def left(self, x: 'Node'):
        self.child[0] = x

    @property
    def right(self) -> 'Node':
        return self.child[1]

    @right.setter
    def right(self, x: 'Node'):
        self.child[1] = x

    # noinspection PyUnusedLocal
    def adjust(self, child: 'Node', delta: int):
        """
        Balance the tree after an insertion or a removal.

        This implementation does nothing: it is intended to be overridden
        in subclasses

        :param child: the child that was updated
        :type child: Node or a subclass of Node
        :param delta: used by subclasses
        :type delta: integer
        :return: returns the new root of the subtree (self in that
            implementation) and the new delta
        :rtype: Tuple[Node, int]
        """
        return self, delta

    # noinspection PyMethodMayBeStatic
    def side(self) -> int:
        """Define the preferred side for searching next node to remove.

        Return -1 for left or 1 for right
        """
        return -1

    def last_child(self, side: int) -> 'Node':
        child = self
        while child.child[side] is not None:
            child = child.child[side]
        return child

    def _rotate(self, side: int) -> 'Node':
        """
        Rotate a subtree to the left is side is 0 else to the right.

        :return: the new root of the subtree (the previous right child)
        :rtype: Node
        """
        node = self.child[1 - side]
        self.child[1 - side] = node.child[side]
        node.child[side] = self
        return node

    def rotate_left(self) -> 'Node':
        """
        Rotate a subtree to the left.

        :return: the new root of the subtree (the previous right child)
        :rtype: Node
        """
        return self._rotate(0)

    def rotate_right(self) -> 'Node':
        """
        Rotate a subtree to the right.

        :return: the new root of the subtree (the previous left child)
        :rtype: Node
        """
        return self._rotate(1)

    def __iter__(self):
        if self.child[0]:
            for k in iter(self.child[0]):
                yield k
        yield self
        if self.child[1]:
            for k in iter(self.child[1]):
                yield k

    def is_valid(self) -> bool:
        """Debugging method to test whether a node is valid.

        This implementation only returns True and is expected to be
        overridden in subclasses for more relevant values
        """
        return self is self


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

    def _insert(self, node: Node, *args) -> Tuple[Node, int]:
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
        else:
            side = 0 if key < node.key else 1
            node.child[side], delta = self._insert(node.child[side], *args)
            node, delta = node.adjust(node.child[side], delta)
        return node, delta

    def _remove(self, node: Node, key: CT) -> Tuple[Node, int]:
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
            if node.child[0] is None:
                self._len -= 1
                return node.child[1], -1
            elif node.child[1] is None:
                self._len -= 1
                return node.child[0], -1
            else:
                side = int(node.side() == 1)
                other = node.child[side].last_child(1 - side)
                node.key = other.key
                if issubclass(self.nodeClass, ValueNode):
                    node.value = cast('ValueNode', other).value
                node.child[side], delta = self._remove(node.child[side], other.key)
                node, delta = node.adjust(node.child[side], delta)
        else:
            side = int(key > node.key)
            node.child[side], delta = self._remove(node.child[side], key)
            node, delta = node.adjust(node.child[side], delta)
        return node, delta

    def _find(self, node, key: CT) -> Optional['Node']:
        if node is None:
            return None
        if node.key == key:
            return node
        return self._find(node.child[key > node.key], key)

    def __len__(self) -> int:
        return self._len

    def __iter__(self):
        return (it.key for it in iter(self.root)
                ) if self.root else iter(tuple())

    def _height(self, node) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.child[i]) for i in range(2))

    def height(self) -> int:
        """
        Returns the height of the tree.

        :return: height of the tree
        :rtype: int
        """
        return self._height(self.root)

    def dump(self) -> None:
        """
        Debugging method that tries to dump a tree.
        """
        msgs = [['' for _ in range(len(self))] for _j in range(self.height())]

        def g(node, level):
            if node.child[0]:
                for kk, ll in g(node.child[0], level + 1):
                    yield kk, ll
            yield node.key, level
            if node.child[1]:
                for kk, ll in g(node.child[1], level + 1):
                    yield kk, ll
        for i, (k, l) in enumerate(g(self.root, 0)):
            msgs[l][i] = str(k)
        for lst in msgs:
            print('\t'.join(lst))

    def is_valid(self) -> bool:
        if self._len != len(tuple(self)):
            return False
        if self.root and not self.root.is_valid():
            return False
        return True


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
        else:
            for it in items:
                self.root, _ = self._insert(self.root, *it)
        for k, v in kwargs.items():
            self.root, _ = self._insert(self.root, k, v)

    def __delitem__(self, key: CT) -> None:
        self.root, _ = self._remove(self.root, key)

    def __getitem__(self, key: CT):
        node = cast(ValueNode, self._find(self.root, key))
        if node is None:
            raise KeyError
        return node.value

    def __setitem__(self, k: CT, v) -> None:
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

    def add(self, key: CT) -> None:
        """
        Inserts a new element in the tree

        :param key: new key
        :type key: a comparable type
        :return: None
        :rtype: NoneType
        """
        self.root, _ = self._insert(self.root, key)

    def discard(self, key: CT) -> None:
        self.root, _ = self._remove(self.root, key)

    def __contains__(self, x: CT) -> bool:
        return self._find(self.root, x) is not None
