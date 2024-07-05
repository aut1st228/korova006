import json
from typing import List, Type
from enum import Enum
from Card import Card
from deck import Deck
from player import Player

class GameStage(Enum):
    PLAY_CARD = 1           # DRAW_CARD, NEXT_TUR
    PLAY_CARD_AGAIN = 2     # NEXT_TURN
    NEXT_TURN = 3           # PLAY_CARD
    END_GAME = 4


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
    def run(self) -> Player:
        """Игра до победы, возвращает игрока-победителя. До этой функции должны быть вызваны или load, или new_game"""
        stage = GameStage.PLAY_CARD
        while stage != GameStage.END_GAME:
            match stage:
                case GameStage.PLAY_CARD:
                    stage = self.try_play_card()
                case GameStage.PLAY_CARD_AGAIN:
                    stage = self.try_play_card(again=True)
                case GameStage.NEXT_TURN:
                    if self.is_win_condition():
                        stage = GameStage.END_GAME
                    else:
                        self.next_player()
                        stage = GameStage.PLAY_CARD
        return self.current_player()

    def try_play_card(self, again: bool = False) -> GameStage:
        """Текущий игрок пытается играть карту с руки. again=True - после того, как уже брал карту из колоды."""
        p: Player = self.current_player()
        card = p.choose_card(self.top, [])
        if card is None:
            return GameStage.NEXT_TURN
        p.hand.remove_card(card)
        self.top = card
        return GameStage.NEXT_TURN



