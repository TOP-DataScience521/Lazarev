cells = []
sequence1 = 'ABCDEFGHabcdefgh'
sequence2 = '12345678'
while True:
    cell = input()
    if len(cell) > 2:
        print('Вы ввели более 2 символов\nПовторите ввод!')
    elif len(cell) < 2:
        print('Вы ввели менее 2 символов\nПовторите ввод!')
    else:
        if cell[0] in sequence1 and cell[1] in sequence2:
            cells.append(cell.lower())
        else:
            print('Вы ввели недопустимый адрес клетки\nПовторите ввод!')
        if len(cells) == 2:
            break
if abs(ord(cells[1][0]) - ord(cells[0][0])) <= 1 and abs(ord(cells[1][1]) - ord(cells[0][1])) <= 1:
    print('да')
else:
    print('нет')


# e2
# f3
# да


# a6
# b4
# нет

