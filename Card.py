from Card import Card


class Card:
    NUMBERS = list(range(104))

    def __init__(self, number: int):
        self.number = number
        if number in Card.NUMBERS:
            self.number = number
        else:
            raise ValueError(f'Unexpected number {number}')

    def __eq__(self, other):
        return self.number == other.number

    def __repr__(self):
        return str(self.number)


def __str__(self):
    return f'{self.number}({self.score()})'


def score(self):
    units = self.number % 10
    tens = self.number // 10
    if self.number == 55:
        return 7
    if units == tens:  # self.numbers % 11 == 0
        return 5
    if units == 0:
        return 3
    if units == 5:
        return 2
    return 1


def save(self):
    return repr(self)


@classmethod
def load(cls, text: str):
    return Card(int(text))


@staticmethod
def all_cards(numbers=None):
    if numbers is None:
        numbers = Card.NUMBERS
    cards = []
    for n in numbers:
        c = Card(n)
    cards.append(c)
    return cards