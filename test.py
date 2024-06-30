import pytest
import random

from scr.card import Card
from scr.deck import Deck

    assert deck.cards == card_list

def test_draw_card():
    deck = Deck(cards=card_list)
    c = deck.draw_card()
    assert str(c) == 'y4'
    assert str(deck) == 'b2 o7'

def test_shuffle():
    random.seed(7)
    deck = Deck.load('y2 y6 y9 b3 b5 b1 g4 g6 g1 g2 o5')
    deck.shuffle()
    assert str(deck) == 'y6 o5 b3 g2 g1 b5 g6 y2 g4 y9 b1'
    deck.shuffle()
    assert str(deck) == 'b3 b5 g1 y2 b1 g6 y9 o5 y6 g2 g4'
    deck.shuffle()
    assert str(deck) == 'o5 y6 g1 g4 b1 y9 g6 y2 b5 g2 b3'
    deck.shuffle()
    assert str(deck) == 'y9 b1 g6 b5 y6 g2 y2 g1 b3 g4 o5'
