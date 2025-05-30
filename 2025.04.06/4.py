def central_tendency(num1: float, num2: float, *numbers: float) -> dict[str, float]:
    """Вычисляет основные меры центральной тенденции для некоторого количества чисел"""
    result = {}
    row = sorted([num1, num2, *numbers])
    if len(row) % 2:
        result['median'] = float(row[len(row)//2])
    else:
        result['median'] = float((row[(len(row)-1)//2] + row[len(row)//2]) / 2)
    result['arithmetic'] = float(sum(row) / len(row))
    mul = 1
    for i in range(len(row)):
        mul *= row[i]
        row[i] = 1 / row[i]
    result['geometric'] = mul ** (1/len(row))
    result['harmonic'] = len(row) / sum(row)
    return result


# >>> central_tendency(12, 5, 8, 4, 11, 9, 3, 18, 21, 30)
# {'median': 10.0, 'arithmetic': 12.1, 'geometric': 9.573419135662855, 'harmonic': 7.51769587503051}
# >>>
# >>> sample = [10, 2, 7, 15, 22, 1, 3, 8, 5, 13]
# >>> central_tendency(*sample)
# {'median': 7.5, 'arithmetic': 8.6, 'geometric': 6.106279193577103, 'harmonic': 3.860653919952176}

