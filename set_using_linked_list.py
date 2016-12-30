class Link(object):
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            return "Link({0}, {1})".format(self.first, repr(self.rest))
        else:
            return "Link({0})".format(self.first)

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

def extend_link(link_1, link_2):
    """
    Combine LINK_1 and LINK_2 to a new Linked List
    >>> l1 = Link(1, Link(2))
    >>> l2 = Link(3, Link(4, Link(5, Link(6))))
    >>> extend_link(l1, l2)
    Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    """
    if link_1 is Link.empty:
        return link_2
    else:
        return Link(link_1.first, extend_link(link_1.rest, link_2))

def filter_link(f, link):
    """Return a link list for which F is true for all its elements
    >>> l1 = Link(1, Link(2, Link(3)))
    >>> odd = lambda x: x % 2
    >>> filter_link(odd, l1)
    Link(1, Link(3))
    """
    if link is Link.empty:
        return link
    else:
        if f(link.first):
            return Link(link.first, filter_link(f, link.rest))
        else:
            return filter_link(f, link.rest)

# Sets as unsorted sequences

def empty(s):
    return s is Link.empty

def contains(s, v):
    """ Return true is set S contains value V

    >>> s = Link(1, Link(2, Link(3)))
    >>> contains(s, 3)
    True
    >>> contains(s, 4)
    False
    """
    if empty(s):
        return False
    if s.first == v:
        return True
    else:
        return contains(s.rest, v)

def adjoin(s, v):
    """ Return a set containing all elements of s and element v

    >>> s = Link(1, Link(2, Link(3)))
    >>> adjoin(s, 1)
    Link(1, Link(2, Link(3)))
    >>> adjoin(s, 4)
    Link(1, Link(2, Link(3, Link(4))))
    """
    if empty(s):
        return Link(v)
    elif s.first == v:
        return s
    else:
        return Link(s.first, adjoin(s.rest, v))

def intersect(set1, set2):
    """ Return the intersections of two sets

    >>> s1 = Link(1, Link(2, Link(3)))
    >>> s2 = Link(3, Link(4))
    >>> s3 = Link(5)
    >>> intersect(s1, s2)
    Link(3)
    >>> intersect(s1, s3)
    ()
    """
    if empty(set1) or empty(set2):
        return Link.empty
    elif contains(set2, set1.first):
        return Link(set1.first, intersect(set1.rest, set2))
    else:
        return intersect(set1.rest, set2)

def union(set1, set2):
    """ Return the union of two sets

    >>> s1 = Link(1, Link(2, Link(3)))
    >>> s2 = Link(3, Link(4))
    >>> s3 = Link(5)
    >>> union(s1, s2)
    Link(1, Link(2, Link(3, Link(4))))
    >>> union(s1, s3)
    Link(1, Link(2, Link(3, Link(5))))
    """
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    elif contains(set2, set1.first):
        return union(set1.rest, set2)
    else:
        return Link(set1.first, union(set1.rest, set2))

# Return set as a ordered sequence

def contains2(s, v):
    """Return true is S contains v

    >>> s = Link(1, Link(2, Link(3)))
    >>> contains2(s, 1)
    True
    >>> contains2(s, 1.5)
    False
    """
    if empty(s):
        return False
    elif s.first == v:
        return True
    elif s.first > v:
        return False
    else:
        return contains2(s.rest, v)

def adjoin2(s, v):
    """ Return a new set containing all values of set s and v

    >>> s = Link(1, Link(2, Link(3)))
    >>> adjoin2(s, 1.5)
    Link(1, Link(1.5, Link(2, Link(3))))
    """
    if empty(s):
        return Link(v)
    elif s.first == v:
        return s
    elif s.first > v:
        return Link(v, s)
    else:
        return Link(s.first, adjoin2(s.rest, v))

def add(s, v):
    """ Add v to s and return s

    >>> s = Link(1, Link(2))
    >>> add(s, 3)
    Link(1, Link(2, Link(3)))
    >>> add(s, 4)
    Link(1, Link(2, Link(3, Link(4))))
    """
    assert not empty(s), "Cannot add to an empty set"
    if s.first == v:
        return s
    elif s.first > v:
        s.rest = adjoin2(s, s.first)
        s.first = v
        return s
    else:
        s.rest = adjoin2(s.rest, v)
        return s
