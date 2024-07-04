from Card import Card
from hand import Hand, CardList


def test_card_list_create():
    cl = CardList(Card(10), Card(33), Card(5))
    assert cl.cards[0] == Card(10)
    assert cl.cards[1] == Card(33)
    assert cl.cards[2] == Card(5)

def test_cl_save():
    cl = CardList(Card(10), Card(33), Card(5))
    assert cl.save() == '10 33 5'

card_list = [Card(2), Card(70), Card(44)]
def test_card_list_load():
    deck = CardList.load("2 70 44")
    assert deck.cards == card_list

def test_add_card():
    cl = CardList(Card(2), Card(70), Card(44))
    cl.add_card(Card(10))
    assert cl.cards[-1] == Card(10)

def test_score():
    cl = CardList(Card(2), Card(70), Card(44))
    assert cl.score() == 9


