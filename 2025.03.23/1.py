numbers = []
while True:
    try:
        num = int(input())
    except ValueError:
        print('Введённая строка не является целым числом')
    else:
        if num % 7:
            break
        else:
            numbers.append(num)
print()
for i in range(len(numbers)-1, -1, -1):
    print(int(numbers[i]), end = ' ')

# 56
# 35
# 98
# 7
# 63
# 85
#
# 63 7 98 35 56