while True:
    numbers = input('Введите 6 цифр номера билета: ')
    if not numbers.isdecimal():
        print('Введённая строка содержит не только цифры!')
    else:
        if len(numbers) > 6:
            print('Введённый номер билета содержит более 6 цифр')
        elif len(numbers) < 6:
            print('Введённый номер билета содержит менее 6 цифр')
        else:
            break
l_sum, r_sum = 0, 0
for i in range(len(numbers)):
    if i < 3:
        l_sum += int(numbers[i])
    else:
        r_sum += int(numbers[i])
print(f'{'да' if l_sum == r_sum else 'нет'}')

# Введите 6 цифр номера билета: 126351
# да
#
# Введите 6 цифр номера билета: 467513
# нет