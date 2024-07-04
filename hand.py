from Card import Card
class CardList:
    def __init__(self, *args):
        self.cards = list(args)

    def __repr__(self):
        return ' '.join(map(repr, self.cards))   # [3, 64, 27, 5]    '3 64 27 5'

    def add_card(self, card):
        self.cards.append(card.value)

    def score(self):
        summ = 0
        for card in self.cards:
            summ += card.score()
        return summ

    def save(self):
        return repr(self)


class Hand(CardList):
    def __init__(self, *args):
        super().__init__(*args)

    def remove_card(self, card):
        self.cards.remove(card.value)

