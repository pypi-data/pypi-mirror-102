#  Copyright (c) 2021  SBA - MIT License

from .bin_tree import Node  # , ValueNode
from . import bin_tree
from enum import Enum


class Color(Enum):
    RED = 0
    BLACK = 1


class RBNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.color = Color.RED

    def adjust(self, child, delta):
        if delta == 1:  # RED addition
            return self, 2 if self.color == Color.RED else 0
        if delta == 2:  # RED violation on child
            other = self._other_child(child)
            if other and (other.color == Color.RED):
                self.color = Color.RED
                self.left.color = self.right.color = Color.BLACK
                return self, 0
            else:
                if child is self.left:
                    if not child.left or child.left.color == Color.BLACK:
                        self.left = child = child.rotate_left()
                    self.rotate_right()
                    child.left.color = Color.BLACK
                else:
                    if not child.right or child.right.color == Color.BLACK:
                        self.right = child = child.rotate_right()
                    self.rotate_left()
                    child.right.color = Color.BLACK
                return child, 0
        other = self._other_child(child)
        if delta == -1:  # child removal
            if child is not None and child.color == Color.RED:
                # was black with red child
                child.color = Color.BLACK
                return self, 0
            if other is None or (other.color == Color.RED
                                 and other.left is None):
                # removal of a red orphan: no violation
                return self, 0
        if delta < 0:  # one level black violation
            if self.color == Color.RED:  # found a black ancestor
                self.color = Color.BLACK
                node = self._paint_red(other)
                return node, 0
            if other.color == Color.RED:  # sibling is red
                if child is self.left:
                    other = self.rotate_left()
                    other.color = Color.BLACK
                    other.left = self._paint_red(self.right)
                    return other, 0
                else:
                    other = self.rotate_right()
                    other.color = Color.BLACK
                    other.right = self._paint_red(self.left)
                    return other, 0
            if ((other.right and other.right.color == Color.RED)
                    or (other.left and other.left.color == Color.RED)):
                # sibling is black with at least a red child
                other = self._paint_red(other)
                other.color = Color.BLACK
                other.left.color = other.right.color = Color.BLACK
                return other, 0
            # sibling is black with 2 black children
            other.color = Color.RED
            return self, -2
        return self, 2 if (self.color == Color.RED
                           and child.color == Color.RED) else 0

    def _paint_red(self, child):
        child.color = Color.RED
        if child.left and child.left.color == Color.RED:
            if child is self.right:
                self.right = child.rotate_right()
                node = self.rotate_left()
                node.right.color = Color.BLACK
            else:
                node = self.rotate_right()
                node.left.color = Color.BLACK
        elif child.right and child.right.color == Color.RED:
            if child is self.left:
                self.left = child.rotate_left()
                node = self.rotate_right()
                node.left.color = Color.BLACK
            else:
                node = self.rotate_left()
                node.right.color = Color.BLACK
        else:
            node = self
        return node

    def side(self):
        return 1 if self.right and self.right.color == Color.RED else -1

    def _other_child(self, child):
        return self.right if child is self.left else self.left


class RBTree(bin_tree.BinTree):
    def _insert(self, node: Node, *args):
        root = node is self.root
        node, delta = super(RBTree, self)._insert(node, *args)
        if root:
            node.color = Color.BLACK
        return node, delta

    def black_height(self):
        h = 0
        node = self.root
        while node is not None:
            if Color.BLACK == node.color:
                h += 1
            node = node.left
        return h


class TreeSet(RBTree, bin_tree.TreeSet):
    def __init__(self, items=tuple(), node_class=RBNode):
        super(TreeSet, self).__init__(items, node_class)


class RBValueNode(bin_tree.ValueNode, RBNode):
    pass


class TreeDict(RBTree, bin_tree.TreeDict):
    def __init__(self, items=(), node_class=RBValueNode, **kwargs):
        super(TreeDict, self).__init__(items, node_class, **kwargs)
