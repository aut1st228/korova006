from Card_class import Card
from Hand_class import Hand


class Row(Hand):
    def six_cards(self, card, player):
        a = self.score()
        player.points += a
        self.cards = [card]