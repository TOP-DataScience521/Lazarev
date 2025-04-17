scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

score = 0
word = input().upper()
for letter in word:
    for key in scores_letters:
        if letter in scores_letters[key]:
            score += key
            break
print(score)


# распределитель
# 20


# конфигурирование
# 27

