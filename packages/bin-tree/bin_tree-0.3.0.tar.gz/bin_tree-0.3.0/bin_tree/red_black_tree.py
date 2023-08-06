#  Copyright (c) 2021  SBA - MIT License

from .bin_tree import Node  # , ValueNode
from . import bin_tree
from enum import Enum
from typing import Optional, Tuple, cast


class Color(Enum):
    RED = 0
    BLACK = 1


class RBNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.color = Color.RED

    def adjust(self, child: Optional['RBNode'], delta) -> Tuple['RBNode', int]:
        if delta == 1:  # RED addition
            return self, 2 if self.color == Color.RED else 0
        if delta == 2:  # RED violation on child
            other = self._other_child(child)
            if other and (other.color == Color.RED):
                self.color = Color.RED
                self.left.color = self.right.color = Color.BLACK
                return self, 0
            else:
                side = child is self.right
                if not child.child[side] or child.child[side].color == Color.BLACK:
                    self.child[side] = child = child._rotate(side)
                self._rotate(1 - side)
                child.child[side].color = Color.BLACK
                return child, 0
        other = self._other_child(child)
        if delta == -1:  # child removal
            if child is not None and child.color == Color.RED:
                # was black with red child
                child.color = Color.BLACK
                return self, 0
            if other is None or (other.color == Color.RED
                                 and other.left is None):
                # removal of a red with no child: no violation
                return self, 0
        if delta < 0:  # one level black violation
            if self.color == Color.RED:  # found a black ancestor
                self.color = Color.BLACK
                node = self._paint_red(other)
                return node, 0
            if other.color == Color.RED:  # sibling is red
                side = int(child is self.right)
                other = self._rotate(side)
                other.color = Color.BLACK
                other.child[side] = self._paint_red(cast(
                    'RBNode', self.child[1 - side]))
                return other, 0
            if any(_ and _.color == Color.RED for _ in other.child):
                # sibling is black with at least a red child
                other = self._paint_red(other)
                other.color = Color.BLACK
                return other, 0
            # sibling is black with 2 black children
            other.color = Color.RED
            return self, -2
        return self, 2 if (self.color == Color.RED
                           and child.color == Color.RED) else 0

    def _paint_red(self, child: 'RBNode') -> 'RBNode':
        child.color = Color.RED
        side = int(child is self.right)
        if child.child[side] is None or child.child[side].color == Color.BLACK:
            if child.child[1 - side] and child.child[1 - side].color == Color.RED:
                self.child[side] = child = child._rotate(side)
            else:
                return self
        child.child[side].color = Color.BLACK
        return self._rotate(1 - side)

    def side(self) -> int:
        return 1 if self.right and self.right.color == Color.RED else -1

    def _other_child(self, child) -> 'RBNode':
        return self.child[child is self.left]

    def is_valid(self) -> bool:
        def black_height(node):
            child_height = black_height(node.child[0]) if node.child[0] else 0
            return int(node.color is Color.BLACK) + child_height
        
        if self.color == Color.RED:
            for _ in self.child:
                if _ and _.color == Color.RED:
                    return False
        return black_height(self.child[0]) == black_height(self.child[1])


class RBTree(bin_tree.BinTree):
    def _insert(self, node: RBNode, *args) -> Tuple['RBNode', int]:
        root = node is self.root
        node, delta = super(RBTree, self)._insert(node, *args)
        if root:
            node.color = Color.BLACK
        return cast('RBNode', node), delta

    def black_height(self) -> int:
        h = 0
        node = self.root
        while node is not None:
            if Color.BLACK == node.color:
                h += 1
            node = node.left
        return h
    
    def is_valid(self) -> bool:
        if self.root and (not self.root.is_valid()
                          or Color.RED == self.root.color):
            return False
        return super(RBTree, self).is_valid()


class TreeSet(RBTree, bin_tree.TreeSet):
    def __init__(self, items=tuple(), node_class=RBNode):
        super(TreeSet, self).__init__(items, node_class)


class RBValueNode(bin_tree.ValueNode, RBNode):
    pass


class TreeDict(RBTree, bin_tree.TreeDict):
    def __init__(self, items=(), node_class=RBValueNode, **kwargs):
        super(TreeDict, self).__init__(items, node_class, **kwargs)
