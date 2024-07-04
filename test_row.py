import pytest
from row import Row

def test_six_cards():
    row = Row()
    player = type('Player', (object,), {'points': 0})
    card = '2 70 44'
    expected_points = 9
    row.six_cards(card, player)
    assert player.points == expected_points


