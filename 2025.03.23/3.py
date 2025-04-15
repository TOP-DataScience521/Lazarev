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
if num % 2:
    i = 3
else:
    i = 2
j = num
sum = num + 1
while i < j:
    if not num % i:
        j = num // i
        sum += i + j
    i += 2
print(f'\n{sum}')


# 65
#
# 84

