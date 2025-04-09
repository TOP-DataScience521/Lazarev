try:
    num = float(input())
except ValueError:
    print('не является числом')
else:
    if num >= 10:
        print('целая часть введённого числа содержит более одного знака')
    elif num ** (1/3) == 2:
        print('да')
    elif num ** (1/2) == 2:
        print('да')
    elif num == 1 or num == 2:
        print('да')
    else:
        print('нет')


# 9
# нет


# 2.5
# нет


# 4
# да


# ++i
# не является числом


# ИТОГ: 5/5

