from scr.card import Card
from scr.card import Hand
import json

class Human:
    """Взаимодествие с человеком."""
    pass

    def choose_card(self, hand: Hand, top: Card, card_counts: list[int]) -> Card | None:
        '''
        Введите какую карту играем из руки: п4
        Такой карты нет в руке
        Введите какую карту играем из руки: g4
        '''
        while True:
            res = input('Введите какую карту играем из руки: ')
            try:
                card = Card.load(res)
                if card in hand.cards:
                    return card
                else:
                    print('Такой карты нет в руке')
            except (ValueError, KeyError, IndexError):
                print('Такой карты не существует')


class AI:
    """Решения принимает бот"""
    pass

    def choose_card(self, hand: Hand, top: Card, card_counts: list[int]) -> Card | None:
        """Выбирает первую подходящую карту с руки, иначе None"""
        # random.choose
        # cards = hand.playable_cards(top) <--

        # cards = []
        # for c in hand.cards:
        #     if top.playable(c):
        #         cards.append(c)
        cards = [c for c in hand.cards if top.playable(c)]
        # if cards:                   # bool([])
        #     return None
        # else:
        #     return cards[0]
        return cards[0] if cards else None
class Player:
    def __init__(self, name: str, hand: Hand = None, is_human: bool=False):
        self.name = name
        self.hand = hand or Hand()
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()
    def __repr__(self):
        return f'{self.name}: {self.hand}'
    def to_dict(self):
        return {
            'name': self.name,
            'hand': self.hand.save(),
            'is_human': isinstance(self.actor, Human)
        }
