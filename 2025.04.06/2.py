def taxi_cost(distance: int, waiting: int = 0) -> int | None:
    """Вычисляет стоимость поездки на такси"""
    cost = 80
    if type(distance) is int and type(waiting) is int and distance >= 0 and waiting >= 0:
        if not distance:
            cost += 80 + waiting * 3
        else:
            cost += (distance / 150) * 6 + waiting * 3
        return round(cost)


# >>> taxi_cost(3668)
# 227
# >>> taxi_cost(5872)
# 315
# >>> taxi_cost(0, 13)
# 199
# >>> taxi_cost(32568, 6)
# 1401
# >>> print(taxi_cost(-155))
# None

