'''создание колоды'''
class Deck:
    def __init__(self, card=None):
        self.cards = []
        for i in range(1, 105):
            self.cards.append(card)

