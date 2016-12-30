def make_withdraw(balance):
    def withdraw(amount):
        if amount > withdraw.balance:
            print("insufficient balance")
        else:
            withdraw.balance -= amount
            return withdraw.balance
    withdraw.balance = balance
    return withdraw

def memo(f):
    """
    Decorator for memoizing
    """
    cache = {}
    def memoize(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return memoize

def count(f):
    """
    Decorator for counting the number of times a function is called
    """
    def counted(n):
        counted.c += 1
        return f(n)
    counted.c = 0
    return counted

@count
@memo
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def g(func):
        nonlocal n
        n = func(n)
        print(n)
        return g
    return g
