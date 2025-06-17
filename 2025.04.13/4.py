def logger(func):
    """Ведёт журнал вызовов декорируемой функции"""
    def wrapper_func(*args, **kwargs):
        try:
            separator = ' -> '
            result = func(*args, **kwargs)
            return result
        except Exception as exception:
            separator = ' .. '
            result = type(exception).__name__ + ': ' + str(exception)
        finally:
            print(func.__name__, end='')
            if len(args) >= func.__code__.co_argcount:
                params = str(args)
            else:
                params = str(args + (() if func.__defaults__ is None else func.__defaults__[(len(args)-func.__code__.co_argcount):]))
            argcount = len(params)
            print(params[:argcount-1], end='')
            if func.__kwdefaults__ is None:
                kwparams = kwargs
            else:
                kwparams = func.__kwdefaults__.copy()
                kwparams.update(kwargs)
            kwargcount = len(kwparams)
            if argcount and kwargcount:
                print(', ', end='')
            for i in range(kwargcount-1):
                print(f'{list(kwparams.keys())[i]}={list(kwparams.values())[i]}', end=', ')
            if kwargcount:
                print(f'{list(kwparams.keys())[kwargcount-1]}={list(kwparams.values())[kwargcount-1]}', end=')')
            print(separator, result, sep='')
    return wrapper_func


@logger
def arithmetic(num1=1, num2=2, num3=3, *numbers, n=3, digits=0):
    """Вычисляет среднее арифметическое для первых 'n' членов последовательности 
    вещественных чисел с точностью, заданной параметром 'digits'"""
    sequence = [num1, num2, num3, *numbers]
    n = len(sequence) if n > len(sequence) else n
    sequence = sequence[:n]
    return round(sum(sequence) / n, digits)


# >>> arithmetic(156, 29, digits=2)
# arithmetic(156, 29, 3, n=3, digits=2) -> 62.67
# 62.67
# >>> arithmetic(5, 12, 38, 11, 16, 25, n=15, digits=5)
# arithmetic(5, 12, 38, 11, 16, 25, n=15, digits=5) -> 17.83333
# 17.83333
# >>> arithmetic()
# arithmetic(1, 2, 3, n=3, digits=0) -> 2.0
# 2.0
# >>> arithmetic('19', 31, 78, n=10)
# arithmetic('19', 31, 78, n=10, digits=0) .. TypeError: unsupported operand type(s) for +: 'int' and 'str'

