def strong_password(password: str) -> bool:
    """Проверяет надёжность пароля"""
    if type(password) is not str:
        raise TypeError('Функция ожидает строку, а передан объект ' + repr(type(password)))
    num_count = 0
    up_case = low_case = printable = False
    if len(password) >= 8:
        for char in password:
            if char.isupper():
                up_case = True
            elif char.islower():
                low_case = True
            elif char.isdecimal():
                num_count += 1
            elif char.isprintable():
                printable = True
    if num_count > 1 and up_case and low_case and printable:
        return True
    else:
        return False


# >>> strong_password('6vr-zpL-mgx-UcL')
# False
# >>> strong_password('k39-wHW-iYX-Zjh')
# True

