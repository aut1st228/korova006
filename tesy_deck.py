import pytest
from deck import Deck
def test_deck_creation():
    deck = Deck()
    assert deck.cards is not None

def test_deck_size():
    deck = Deck()
    assert len(deck.cards) == 104
