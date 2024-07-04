import pytest
from Hand_class import Hand
from Card_class import Card

card3 = Card("A")
hand.add_card(card3)
assert hand.score() == 31

card4 = Card("2")
hand.add_card(card4)
assert hand.score() == 33

card5 = Card("5")
hand.add_card(card5)
assert hand.score() == 38

card6 = Card("10")
hand.add_card(card6)
assert hand.score() == 48
