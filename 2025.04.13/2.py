def deck():
    """Создаёт упорядоченную колоду карт"""
    result = []
    suits = ['черви', 'бубны', 'пики', 'трефы']
    for suit in suits:
        for i in range(2, 15):
            result.append((i, suit))
    for elem in result:
        yield elem


# >>> list(deck())[2::10]
# [(4, 'черви'), (14, 'черви'), (11, 'бубны'), (8, 'пики'), (5, 'трефы')]

