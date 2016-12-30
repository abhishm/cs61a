def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


f_1 = lambda n: f_then_g(f_1, g, n // 10)
f_2 = lambda n: f_then_g(g, f_2, n // 10)
g = lambda n: print(n)

grow = lambda n: f_then_g(f_1, g, n // 10)
shrink = lambda n: f_then_g(g, f_2, n // 10)

# def grow(n):
#     if n // 10:
#         grow(n // 10)
#         print(n // 10)
#
# def shrink(n):
#     if n // 10:
#         print(n // 10)
#         shrink(n // 10)
