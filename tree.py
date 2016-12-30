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


def memo(f):
    cache = {}
    def memoize(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return memoize

def print_tree(t, indent=0):
    if t.is_leaf():
        print(" " * indent + str(t.root))
    else:
        print(" " * indent + str(t.root))
        for b in t.branches:
            print_tree(b, indent + 1)

@memo
def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left_tree = fib_tree(n - 2)
        right_tree = fib_tree(n - 1)
        root = left_tree.root + right_tree.root
        return Tree(root, [left_tree, right_tree])

def leaves(t):
    if t.is_leaf():
        return [t.root]
    else:
        return sum([leaves(b) for b in t.branches], [])

def prune_tree(t, n):
    """
    prune sub-trees whose root value is n and do it in-place
    >>> t = fib_tree(5)
    >>> prune_tree(t, 1)
    >>> print(t)
    5
      2
      3
        2
    """

    t.branches = [b for b in t.branches if b.root != n] ### no need to worry about the root node because the question says about the sub-trees
    for b in t.branches:
        prune_tree(b, n)


def prune_repeats(t, seen):
    """
    prune all the sub-trees in t that has already been seen
    >>> t = Tree(2, [Tree(2)])
    >>> prune_repeats(t)
    Tree(2)
    """
    t.branches = [b for b in t.branches if b not in seen]
    seen.append(t)
    for b in t.branches:
        prune_repeats(b, seen)

def hailstone(n):
    """
    print a hailstone sequence and return its length
    """
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(3 * n + 1)

def hailstone_tree(k, n=1):
    """
    Build a tree in which paths are hailstone sequence
    This hailstone tree should start with N and and its depth should be K.
    >>> hailstone_tree(3, 1)
    Tree(1, Tree(2, Tree(4)))
    """
    if k == 1:
        return Tree(n)
    elif (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1 and n > 4:
        return Tree(n, [hailstone_tree(k - 1, 2 * n), hailstone_tree(k - 1, (n - 1) // 3)])
    else:
        return Tree(n, [hailstone_tree(k - 1, 2 * n)])


def longest_path_below(t, k):
    """Return the longest path in T with all values less than k
    >>> t = Tree(1, [Tree(3, [Tree(4)]), Tree(2)])
    >>> longest_path_below(t, 3)
    Tree(1, [Tree(2)])
    >>> longest_path_below(t, 5)
    Tree(1, [Tree(3, [Tree(5)])])
    """
    longest_paths = [longest_path_below(b, k) for b in t.branches]
    if t.is_leaf():
        if t.root < k:
            return [t.root]
        else:
            return []
    else:
        longest_path = max(longest_paths, key = len)
        if t.root < k:
            return [t.root] + longest_path
        else:
            return longest_path
