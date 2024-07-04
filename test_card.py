import pytest
from deck import Card

def test_card_creation():
    c = Card(50)
    assert c.number == 50

def test_card_equality():
    c1 = Card(30)
    c2 = Card(30)
    assert c1 == c2

def test_card_repr():
    c = Card(70)
    assert repr(c) == '70'

def test_save_method():
    c = Card(90)
    assert c.save() == '90'

def test_all_cards():
    cards = Card.all_cards()
    assert len(cards) == 104
