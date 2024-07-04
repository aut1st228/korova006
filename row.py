from hand import CardList


class Row(CardList):
    def six_cards(self, card, player):
        a = self.score()
        player.points += a
        self.cards = [card]