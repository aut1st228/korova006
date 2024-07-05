from row import Row
from hand import Card
from player import Player


def test_six_cards(points=None):
    row = Row()
    player = Player(points)
    card1 = Card(2)
    card2 = Card(70)
    card3 = Card(44)

    row.add_card(card1)
    row.add_card(card2)
    row.add_card(card3)

    row.six_cards(card3, player)

    assert player.points == 9



