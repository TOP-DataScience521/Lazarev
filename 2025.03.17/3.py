year = int(input())
if year % 100 and not year % 4 or not year % 400:
    print('да')
else:
    print('нет')

# 2000
# да

# 1900
# нет