class Tree(object):
    """
    A Tree has a root node and it has branches.
    The branches should be an object of the Tree class.
    """
    def __init__(self, root, branches=[]):
        assert all(isinstance(b, Tree) for b in branches), "all branches should be a Tree object"
        self.root = root
        self.branches = list(branches) #Creating a copy of branches

    def root(self):
        return self.root

    def branches(self):
        return self.branches

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.is_leaf():
            return "Tree({0})".format(self.root)
        else:
            return "Tree({0}, {1})".format(self.root, repr(self.branches))

    def __str__(self):
        return "\n".join(self.indent())

    def indent(self, indentation=0):
        indented = ["  " * indentation + str(self.root)]
        for b in self.branches:
            indented.extend(b.indent(indentation + 1))
        return indented

    def __eq__(self, other):
        if self.root != other.root:
            return False
        elif len(self.branches) != len(other.branches):
            return False
        else:
            for b1, b2 in zip(self.branches, other.branches):
                if b1 != b2: return False
            return True

def leaves(t):
    if t.is_leaf():
        return [t.root]
    else:
        return sum([leaves(b) for b in t.branches], [])

# Binary Trees

class BTree(Tree):
    """ A tree with exactly two branches, which may be empty. """
    empty = Tree(None)

    def __init__(self, root, left=empty, right=empty):
        Tree.__init__(self, root, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return "BTree({0})".format(self.root)
        elif self.right is BTree.empty:
            return "BTree({0}, {1})".format(self.root, repr(self.left))
        else:
            if self.left is BTree.empty:
                return "BTree({0}, {1}, {2})".format(self.root, "BTree.empty", repr(self.right))
            return "BTree({0}, {1}, {2})".format(self.root, repr(self.left), repr(self.right))

def fib_tree(n):
    """ Fibonacci Binary Tree

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 1 or n == 0:
        return BTree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return BTree(left.root + right.root, left, right)

def contents(t):
    """Return the values in a binary Tree

    >>> contents(BTree.empty)
    []
    >>> t = BTree(1, BTree(2), BTree(3, BTree.empty, BTree(4)))
    >>> contents(t)
    [2, 1, 3, 4]
    """
    if t is BTree.empty:
        return []
    else:
        left_content = contents(t.left)
        right_content = contents(t.right)
        total_content = left_content + [t.root] + right_content
        return total_content

def bst(values):
    """ Create a balanced binary search tree from a sorted list

    >>> bst([1, 3, 5, 7, 9, 11, 13])
    BTree(7, BTree(3, BTree(1), BTree(5)), BTree(11, BTree(9), BTree(13)))
    """
    if len(values) == 0:
        return BTree.empty
    else:
        mid = len(values) // 2
        root = values[mid]
        left = bst(values[:mid])
        right = bst(values[mid + 1:])
        return BTree(root, left, right)

def largest(t):
    """ Retrun the largest element in the binary tree T

    >>> t = bst([1, 3, 5, 7, 9, 11, 13])
    >>> largest(t)
    13
    """
    if t.right is BTree.empty:
        return t.root
    else:
        return largest(t.right)

def second_largest(t):
    """ Return the second largest element in the binary tree T

    >>> t = bst([1, 3, 5, 7, 9, 11, 13])
    >>> second_largest(t)
    11
    """
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.root
    else:
        return second_largest(t.right)

def contains(s, v):
    """ Return true if set s contains value v.

    >>> s = BTree(1, BTree(2, BTree(3)))
    >>> contains(s, 1)
    True
    """
    if s is BTree.empty:
        return False
    elif s.root == v:
        return True
    elif s.root < v:
        return contains(s.right, v)
    else:
        return contains(s.left, v)

def adjoin(s, v):
    """ Return a set containing all elements of s and element v

    >>> b = bst(range(1, 10, 2)) # [1, 3, 5, 7, 9]
    >>> adjoin(b, 6)
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7, BTree(6))))
    """
    if s is BTree.empty:
        return BTree(v)
    elif s.root == v:
        return s
    elif s.root < v:
        return BTree(s.root, s.left, adjoin(s.right, v))
    elif s.root > v:
        return BTree(s.root, adjoin(s.left, v), s.right)
