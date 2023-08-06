#  Copyright (c) 2021  SBA - MIT License

from .bin_tree import Node, ValueNode
from . import bin_tree
from typing import cast, Tuple


class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.weight = 0

    def rotate_left(self) -> 'AVLNode':
        node = self.right
        self.weight -= 1
        if node.weight > 0:
            self.weight -= node.weight
        node.weight -= 1
        if self.weight < 0:
            node.weight += self.weight
        return cast('AVLNode', super().rotate_left())

    def rotate_right(self) -> 'AVLNode':
        node = self.left
        self.weight += 1
        if node.weight < 0:
            self.weight -= node.weight
        node.weight += 1
        if self.weight > 0:
            node.weight += self.weight
        return cast('AVLNode', super().rotate_right())

    def side(self) -> int:
        return 1 if self.weight >= 0 else -1

    def adjust(self, child, delta) -> Tuple['AVLNode', int]:
        if child == self.left:
            self.weight -= delta
        else:
            self.weight += delta
        if delta > 0 and self.weight == 0:
            delta = 0
        if delta < 0 and self.weight != 0:
            delta = 0
        if self.weight == 2:
            if self.right.weight < 0:
                self.right = self.right.rotate_right()
            return self.rotate_left(), 0
        elif self.weight == -2:
            if self.left.weight > 0:
                self.left = self.left.rotate_left()
            return self.rotate_right(), 0
        else:
            return self, delta

    def is_valid(self) -> bool:
        def height(node: bin_tree.Node) -> int:
            if node is None:
                return 0
            return 1 + max(height(node.child[_]) for _ in range(2))

        for i in range(2):
            if self.child[i] and not self.child[i].is_valid():
                return False
        if not -1 <= self.weight <= 1:
            return False
        return self.weight == height(self.child[1]) - height(self.child[0])


class AVLValueNode(ValueNode, AVLNode):
    pass


class TreeSet(bin_tree.TreeSet):
    def __init__(self, items=tuple(), node_class=AVLNode):
        super().__init__(items, node_class)


class TreeDict(bin_tree.TreeDict):
    def __init__(self, items=(), node_class=AVLValueNode, **kwargs):
        super(TreeDict, self).__init__(items, node_class, **kwargs)
