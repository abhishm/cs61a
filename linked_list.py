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

l1 = Link(1, Link(2, Link(3)))
l2 = Link(4, Link(5, Link(6)))

square = lambda x: x ** 2

odd = lambda x: x % 2 == 1

def extend_link(link_1, link_2):
    """
    Combine LINK_1 and LINK_2 to a new Linked List
    >>> extend_link(l1, l2)
    Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    """
    if link_1 is Link.empty:
        return link_2
    else:
        return Link(link_1.first, extend_link(link_1.rest, link_2))

def join_link(link, seperator):
    """
    Join the LINK using SEPERATOR
    >>> join_link(l1, ", ")
    '1, 2, 3'
    """
    if link is Link.empty:
        return ""
    elif link.rest is Link.empty:
        return str(link.first)
    else:
        return str(link.first) + seperator + join_link(link.rest, seperator)

def map_link(f, link):
    """
    Map function F to LINK
    >>> map_link(square, l1)
    Link(1, Link(4, Link(9)))
    """
    if link is Link.empty:
        return link
    else:
        return Link(f(link.first), map_link(f, link.rest))

def reverse_link(link):
    """
    Reverse a linked list
    >>> reverse_link(l1)
    Link(3, Link(2, Link(1)))
    """
    if link is Link.empty:
        return link
    else:
        return extend_link(reverse_link(link.rest), Link(link.first))

def reverse_link2(link):
    """ Reverse a linked list using an iterative approach and does it inplace
    >>> link = Link(1, Link(2, Link(3)))
    >>> link = reverse_link2(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    prev = Link.empty
    while link is not Link.empty:
        _next = link.rest
        link.rest = prev
        prev = link
        link = _next
    return prev

def reverse_link3(link):
    """ Reverse a linked list using a recursive approach and do not destroy the
    original linked_list
    >>> link = Link(1, Link(2, Link(3)))
    >>> link = reverse_link3(link)
    >>> link
    Link(3, Link(2, Link(1)))
    """
    def reverse_link_helper(prev, rest):
        if prev is Link.empty:
            return rest
        else:
            return reverse_link_helper(prev.rest, Link(prev.first, rest))
    return reverse_link_helper(link, Link.empty)

def partition(n, m):
    """
    Save all the partition of N using all the integers upto M in a linked list
    """
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m <= 0:
        return Link.empty
    else:
        using_m = partition(n - m, m)
        with_m = map_link(lambda p: Link(m, p), using_m)
        without_m = partition(n, m - 1)
        return extend_link(without_m, with_m)


def separate_linked_list(mixed_link, straight_link):
    """MIXED_LINK was a good linked list but somehow its last node was
    assigned to a node of the straight_link. Fixed the linked list
    >>> link1 = Link(1, Link(2, Link(3)))
    >>> link2 = Link(10, Link(20, Link(30)))
    >>> link1.rest.rest.rest = link2.rest # mixing the first link
    >>> separate_linked_list(link1, link2)
    >>> link1.rest.rest.rest == Link.empty
    True
    """
    
