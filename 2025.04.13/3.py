from random import (
    choice,
    randrange as rr
)

def tree_generator(level=0) -> list:
    """Генерирует дерево с произвольным количеством веток и листьев"""
    result = []
    
    # Максимальный уровень вложенности
    depth = 5
    
    # Максимальное количество листьев на ветке и веток на дереве
    cnt = 5
    
    # Вероятность появления листьев и веток ставлю в обратную зависимость.
    # С увеличением уровня вложенности вероятность появления веток убывает,
    # вероятность появления листьев возрастает. На нулевом уровне
    # возможность появления листьев исключается.
    prob = [0]*(depth-level) + [1]*level
    
    start = 0 if level else 1
    
    for _ in range(rr(start, cnt+1)):
        elem = 'leaf' if choice(prob) else tree_generator(level+1)
        result.append(elem)
    
    return result


# >>> tree_generator()
# [[[['leaf', ['leaf'], 'leaf'], ['leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf', 'leaf', 'leaf']]], ['leaf', ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], ['leaf'], 'leaf'], ['leaf', 'leaf', 'leaf', ['leaf', 'leaf'], ['leaf', 'leaf']]], [[]]]]
# >>> tree_generator()
# [[[]]]
# >>> tree_generator()
# [[['leaf'], [[]], 'leaf', ['leaf']], []]

