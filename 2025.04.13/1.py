def tree_leaves(branches) -> int:
    """Считает количество листьев на дереве"""
    count = 0
    for branch in branches:
        if type(branch) in (list, tuple, set):
            count += tree_leaves(branch)
        elif type(branch) == str and branch == 'leaf':
            count += 1
    return count


# >>> tree = ['leaf', 'leaf', [[[['leaf', 'leaf'], 'leaf'], [['leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', ['leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']], 'leaf']
# >>>
# >>> tree_leaves(tree)
# 33

