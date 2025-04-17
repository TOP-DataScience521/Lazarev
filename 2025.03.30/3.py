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
            # Вычисляем разность букв и добавляем цифру
            # Белые клетки будут чётными, чёрные нечётными
            # В список заносим только результат вычислений
            cells.append((ord(cell[0].lower()) - ord('a') + int(cell[1])) % 2)
        else:
            print('Вы ввели недопустимый адрес клетки\nПовторите ввод!')
        if len(cells) == 2:
            break
if cells[0] == cells[1]:
    print('да')
else:
    print('нет')


# b1
# d5
# да


# h6
# e8
# нет

