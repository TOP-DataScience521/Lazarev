while True:
    try:
        cnt = int(input())
    except ValueError:
        print('Введённая строка не является целым числом')
    else:
        if cnt < 1:
            print('Введённое число не является натуральным')
        else:
            break
a, b = 1, 1
for i in range(cnt-1):
    print(a, end=', ')
    a, b = b, a+b
else:
    print(a)


# 13
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233


# 5
# 1, 1, 2, 3, 5

