import pytest
from Card import Card
def test_card_creation():
    c = Card(50)
def test_card_equality():
    c2 = Card(30)
    assert c1 == c2
    c3 = Card(47)
    assert c1 != c3
    assert c3 != c1

def test_card_repr():
    c = Card(70)
    assert repr(c) == '70'
    assert str(c) == '70(3)'

def test_save_method():
    c = Card(90)
    assert c.save() == '90'


def test_all_cards():
    cards = Card.all_cards([1, 4, 7])
    assert len(cards) == 3
    cards = Card.all_cards()
    assert len(cards) == 104

def test_cow_penalty_points():
    assert Card(55).score() == 7
    assert Card(33).score() == 5
    assert Card(70).score() == 3
    assert Card(25).score() == 2
    assert Card(7).score() == 1
