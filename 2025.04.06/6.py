base_dict = {chr(i):i-ord('0') for i in range(ord('0'), ord('9')+1)}
base_dict.update({chr(i):i-ord('a')+10 for i in range(ord('a'), ord('z')+1)})

def to_dec(value: str, base: int) -> str | None:
    """Преобразовывает число из произвольной системы счисления в десятичную"""
    if type(value) is not str or type(base) is not int:
        return

    if len(value) and 2 <= base <= 36:
        sign = ''
        value = value.lower()
        if value[0] in {'+', '-'}:
            sign = value[0]
            value = value[1:]
        value = value.replace(',', '.')
        value = value.rstrip('.')
        if value[0] == '.':
            value = '0' + value
        base_set = set(base_dict) | {'.'}
        if set(value) | base_set != base_set or value.count('.') > 1:
            # Введённая строка не является числом
            return

        base_set = set([i for i in base_dict if base_dict[i] < base]) | {'.'}
        if set(value) | base_set != base_set:
            # Число не соответствует указанной системе счисления
            return

        for i in range(len(value)):
            if value[i] == '.':
                i -= 1
                break
        result = 0
        for digit in value:
            if digit == '.':
                continue
            result += base_dict[digit.lower()] * base ** i
            i -= 1
        else:
            return sign + str(result)


def from_dec(value: str, base: int, digits: int) -> str | None:
    """Преобразовывает число из десятичной системы счисления в произвольную"""
    if type(value) is not str or type(base) is not int:
        return

    if len(value) and 2 <= base <= 36:
        sign = ''
        if value[0] in {'+', '-'}:
            sign = value[0]
            value = value[1:]
        value = value.replace(',', '.')
        value = value.rstrip('.')
        if value[0] == '.':
            value = '0' + value
        base_set = set(base_dict) | {'.'}
        if set(value) | base_set != base_set or value.count('.') > 1:
            # Введённая строка не является числом
            return

        base_set = set([i for i in base_dict if base_dict[i] < 10]) | {'.'}
        if set(value) | base_set != base_set:
            # Число не является десятичным
            return

        rem_list = []
        value_list = value.split('.')
        result = ''
        if len(value_list[0]):
            value = int(value_list[0])
            while True:
                value, rem = divmod(value, base)
                rem_list.append(list(base_dict.keys())[rem])
                if not value:
                    rem_list.reverse()
                    result = ''.join(rem_list)
                    break
        if len(value_list) > 1 and len(value_list[1]):
            value = float('.' + value_list[1])
            result += '.'
            for _ in range(digits):
                value *= base
                result += list(base_dict.keys())[int(value)]
                value -= int(value)
                if not value:
                    break
        if result:
            return result


def int_base(value: str, base_from: int, base_to: int) -> str | None:
    """Преобразовывает число из произвольной системы счисления в произвольную"""
    value = to_dec(value, base_from)
    result = from_dec(value, base_to, 8)
    return result


# >>> int_base('18DAF110', 16, 2)
# '11000110110101111000100010000'
# >>> int_base('11101001', 2, 36)
# '6h'

