list = []
i = 0
while True:
    list.append(input().split(' '))
    if '' in list[i]:
        list[i].remove('')
    try:
        for j in range(len(list[i])):
            list[i][j] = int(list[i][j])
    except ValueError:
        print('Вы ввели недопустимое значение\nПопробуйте ещё раз!')
        del(list[i])
    else:
        i += 1
        if len(list) == 2:
            break
Result = False
for i in range(len(list[0])-len(list[1])+1):
    if list[0][i:i+len(list[1])] == list[1]:
        Result = True
        break
if Result:
    print('да')
else:
    print('нет')


# 5 2 6 12 458 1634
# 6 12 458
# да


# 1 2 5 9 6 8
#
# да


# 5 3 8 1 6 7
# 8 1 1
# нет

