'''создание колоды'''
import random

from Card import Card


class Deck:
    def __init__(self, card=None):
        self.cards = []
        for i in range(1, 105):
            self.cards.append(card)

    def shuffle(self):
        """Перемешать колоду."""
        random.shuffle(self.cards)

    def save(self):
        return repr(self)

    @classmethod
    def load(cls, text: str):
        words = text.split()
        cards = []
        for w in words:
            c = Card.load(w)
            cards.append(c)

        # cards = [Card.load(w) for w in words]

        deck = Deck(cards=cards)
        return deck


