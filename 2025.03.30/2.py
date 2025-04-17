fruit_list = []
while True:
    fruit = input()
    if len(fruit):
        fruit_list.append(fruit)
    else:
        fruits = ' и '.join(fruit_list)
        fruits = fruits.replace(' и ', ', ', len(fruit_list)-2)
        print(fruits)
        break


# апельсин
#
# апельсин


# яблоко
# груша
#
# яблоко и груша


# виноград
# арбуз
# дыня
#
# виноград, арбуз и дыня


# персик
# гранат
# грейпфрут
# виноград
#
# персик, гранат, грейпфрут и виноград

