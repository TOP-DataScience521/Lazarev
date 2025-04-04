while True:
    try:
        num = int(input())
    except ValueError:
        print('Введённая строка не является целым числом')
    else:
        if num < 1:
            print('Введённое число не является натуральным')
        else:
            break
a = int('1' + '0' * (num - 1)) + 1
b = int('1' + '0' * num)
cnr = 0
# Для уменьшения кол-ва итераций перебираем только нечётные числа
if not a % 2:
    a = 3
    cnr = 1
for i in range(a, b, 2):
    j = 3
    while j < i:
        if not i % j:
            break
        j += 2
    else:
        cnr += 1
print(f'\n{cnr}')

# 4
#
# 1061