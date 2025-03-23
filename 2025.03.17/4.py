try:
    num = float(input())
except ValueError:
    print('не является числом')
else:
    if num >= 10:
        print('целая часть введённого числа содержит более одного знака')
    elif num > 4 and 2 ** 3 == num:
        print('да')
    elif num > 2 and 2 ** 2 == num:
        print('да')
    elif num in [1, 2]:
        print('да')
    else:
        print('нет')

# 9
# нет
#
# 2.5
# нет
#
# 4
# да
#
# ++i
# не является числом