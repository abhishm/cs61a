def contains(a, b):
    """Return True if A contains B in order
    >>> contains(iter("abcd"), iter("bc"))
    True
    >>> contains(iter("abhishek"), iter("hongmei"))
    False
    """
    for k in b:
        try:
            while k != next(a):
                pass
        except StopIteration:
            return False
    return True

class countdown_iterator:
    def __init__(self, k):
        self.k = k
    def __iter__(self):
        while self.k > 0:
            yield self.k
            self.k -= 1

def countdown(k):
    """countdown from k to 1
    Use "yield from" : yield from is a key word used in yielding text from an iterable
    >>> list(countdown(4))
    [4, 3, 2, 1]
    """
    if k > 0:
        yield k
        yield from countdown(k - 1)

def prefixes(s):
    """Return all prefixes of s
    >>> list(prefixes("abcd"))
    ["a", "ab", "abc", "abcd"]
    """
    if s:
        yield from prefixes(s[:-1])
        yield s

def sub_strings(s):
    """Return all substring of s
    >>> list(sub_strings("abcd"))
    ["a", "ab", "abc", "abcd", "b", "bc", "bcd", "c", "cd", "d"]
    """
    if s:
        yield from prefixes(s)
        yield from sub_strings(s[1:])
