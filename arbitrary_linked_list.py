"""
In this file, I will be solving the problem given by Hongmei.
I am given a linked list. In this linked list, there are usual
next connections and also there are arbitrary connections.
"""

class RandomLink(object):
    empty = ()
    def __init__(self, first, rest=empty, random=empty):
        self.first = first
        self.rest = rest
        self.random = random

    def __str__(self):
        if not self.rest:
            if self.random:
                return "({0}, {1}, {2})".format(str(self.first), (), str(self.random.first))
            else:
                return "{0}, {1}, {2}".format(str(self.first), (), ())
        else:
            if self.random:
                return "({0}, {1}, {2}), {3}".format(str(self.first), (self.rest.first), str(self.random.first), str(self.rest))
            else:
                return "({0}, {1}, {2}), {3}".format(str(self.first), (self.rest.first), (), str(self.rest))

    def copy(self):
        if self.rest:
            return RandomLink(self.first, self.rest.copy())
        else:
            return RandomLink(self.first)

t1 = RandomLink(1)
t2 = RandomLink(2)
t3 = RandomLink(3)
t4 = RandomLink(4)
t5 = RandomLink(5)

t1.rest = t2
t2.rest = t3
t3.rest = t4
t4.rest = t5

t1.random = t3
t2.random = t5
t4.random = t3
t5.random = t2
