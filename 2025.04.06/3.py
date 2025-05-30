def countable_nouns(number: int, nouns: tuple[str, str, str]) -> str:
    """Возвращает существительное русского языка, согласованное с числом"""
    if type(number) is not int:
        raise TypeError('Функция в первом аргументе ожидает целое число, а передан объект ' + repr(type(number)))
    if len(nouns) == 3:
        result = ""
        remainder = number % 10
        if remainder in {0, 5, 6, 7, 8, 9} or number in {11, 12, 13, 14}:
            result = nouns[2]
        elif remainder in {2, 3, 4}:
            result = nouns[1]
        elif remainder:
            result = nouns[0]
        if type(result) is not str:
            raise TypeError('Функция ожидает строку, а передан объект ' + repr(type(result)))
        return result
    else:
        raise TypeError('Функция countable_nouns() принимает 4 аргумента, а передано ' + str(len(nouns)+1))


# >>> countable_nouns(331, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(23, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(15, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(20, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(4, ("год", "года", "лет"))
# 'года'

