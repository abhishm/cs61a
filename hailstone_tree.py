def tree(root, branches=[]):
    return [root] + list (branches)

# Selectors

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    print("  " * indent + str(root(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def hailstone_tree(n, h):
    """
    generate a tree of height h that shows hailstone numbers reaching to number
    n and the height of the tree is h
    """
    if h == 0:
        return tree(n)
    else:
        branches = [hailstone_tree(2 * n, h - 1)]
        if ((n - 1) % 3 == 0) and (n not in [1, 4]):
            branches.append(hailstone_tree((n - 1) // 3, h - 1))
        return tree(n, branches)
