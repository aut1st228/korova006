from Card_class import Card


class Hand:
    def __init__(self, *args):
        self.cards = []
        for i in args:
            self.cards.append(i.value)

    def __repr__(self):
        cards = []
        for i in self.cards:
            cards.append(i)
        return str(cards)

    def add_card(self, card):
        self.cards.append(card.value)

    def remove_card(self, card):
        self.cards.remove(card.value)

    def score(self):
        summ = 0
        for i in self.cards:
            summ += Card(i).point
        return summ
