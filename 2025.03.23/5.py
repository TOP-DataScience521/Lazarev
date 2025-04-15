msg = input()
sum = 0
for i in msg:
    if i.isalpha() or i.isdecimal():
        sum += 30
print(f'{sum // 100} руб. {(sum % 100):02} коп.')


# Важно не то, что с вами происходит, а то, как вы на это реагируете!
# 15 руб. 00 коп.

