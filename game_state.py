import json
from typing import List, Type

from Card import Card
from deck import Deck
from player import Player

class GameState:
    def __init__(self, players=list[Player], iplayer: int = 0, deck: Deck = None):
        self.players = players
        self.iplayer = iplayer
        if deck is None:
            deck = Deck(Card.all_cards())
            deck.shuffle()

        self.deck = deck

        # если у всех игроков нет карт, это новая игра, раздадим по 10 карт всем
        for p in self.players:
            for _ in range(10):
                p.hand.add_card(self.deck)

    def current_player(self) -> Type[list[Player]]:
        return self.players[self.iplayer]

    def save(self) -> dict:
        return {
            'players': [p.save() for p in self.players],
            'current_player_index': self.iplayer,
            'deck': self.deck.save()
        }

    @classmethod
    def load(cls, text):
        data = json.loads(text)
        return cls(players=[Player.load(pd) for pd in data['players']],
                   iplayer=data['current_player_index'],
                   deck=Deck.load(data['deck']))

    @classmethod
    def new_game(cls, players: list[Player]):
        game = cls(players)




