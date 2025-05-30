def orth_triangle(*, cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
    """Вычисляет третью сторону прямоугольного треугольника по двум переданным"""
    if type(cathetus1) in [int, float] and type(cathetus2) in [int, float] and type(hypotenuse) in [int, float]:
        if cathetus1 > 0 and cathetus2 > 0 and not hypotenuse:
            return (cathetus1 ** 2 + cathetus2 ** 2) ** (1/2)
        if 0 < cathetus2 < hypotenuse and not cathetus1:
            return (hypotenuse ** 2 - cathetus2 ** 2) ** (1/2)
        if 0 < cathetus1 < hypotenuse and not cathetus2:
            return (hypotenuse ** 2 - cathetus1 ** 2) ** (1/2)


# >>> orth_triangle(cathetus1=3, cathetus2=4)
# 5.0
# >>> orth_triangle(cathetus1=15, hypotenuse=17)
# 8.0
# >>> print(orth_triangle(cathetus1=10))
# None
# >>> print(orth_triangle(cathetus2=10, hypotenuse=8))
# None

