HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    store = {}
    if n in store:
        return store[n]
    elif n <= 3:
        store[n] = n
        return n
    else:
        store[n] = g(n-1) + 2 * g(n-2) + 3 * g(n-3)
        return store[n]

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    vals = [1, 2, 3]
    if n <= 3:
        return vals[n-1]
    for i in range(n - 3):
        new_val = 3 * vals[0] + 2 * vals[1] + 1 * vals[2]
        vals = vals[1:] + [new_val]
    return vals[-1]


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # elem = 0
    # count_up = 1
    # for k in range(1, n + 1):
    #     if count_up:
    #         elem += 1
    #     else:
    #         elem -= 1
    #     if k % 7 == 0 or has_seven(k):
    #         count_up = 1 - count_up

    def count_direction(present_direction, k):
        if k % 7 == 0 or has_seven(k):
            return 1 - present_direction
        else:
            return present_direction

    def ping(k, elem, count_up):
        if k == n:
            return elem
        else:
            return ping(k + 1, elem + (2 * count_up - 1), count_direction(count_up, k + 1))


    return ping(1, 1, 1)



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def counts(amount, least_denomination):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif amount == 0:
            return 0
        elif amount < 2 ** least_denomination:
            return 0
        else:
            return counts(amount - 2 ** least_denomination, least_denomination) + counts(amount, least_denomination + 1)

    return counts(amount, 0)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n: 1 if n == 1 else mul(n, make_anonymous_factorial()(sub(n, 1)))
