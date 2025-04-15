sum, cnt, i = 0, 0, 0
while True:
    try:
        if cnt < 1:
            cnt = int(input())
        else:
            num = int(input())
    except ValueError:
        print('Введённая строка не является целым числом')
    else:
        if cnt < 1:
            print('Введённое число не является натуральным')
        else:
            if i and num > 0:
                sum += num
            i += 1
        if i > cnt and cnt > 0:
            break
print(f'\n{sum}')


# 9
# -25
# 4
# 19
# -66
# -3
# 32
# 1
# 13
# -30
#
# 69

