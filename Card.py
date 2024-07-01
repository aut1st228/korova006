from deck import Card


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
        return f'{self.number}'

    def save(self):
        return repr(self)

    @staticmethod
    def all_cards(umbers=None, numbers=None):
        """Возвращает все карты.
        :param colors:
        :param numbers:
        """
        if numbers is None:
            numbers = Card.NUMBERS
            cards = []
            for n in numbers:
                c = Card( n)
                cards.append(c)

                # return [Card(col, n) for col in colors for n in numbers]
        return cards