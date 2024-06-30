from deck import Card


class Card:

    COLORS = ['orange', 'green', 'blue', 'yellow']
    NUMBERS = list(range(1, 104)) + list(range(1, 104))

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return f'{self.color[0]}{self.number}'


    def create(short_form: str) -> Card:
        color = short_form[0]
        number = int(short_form[1])
        return Card(color, number)
    def list_from_str(text: str) -> list[Card]:
        return [Card.create(s) for s in text.split()]

class Hand(CardList):
    def __init__(self, cards: list[Card]):
        super(Hand, self).__init__(cards)

    def playable_cards(self, top: Card) -> list[Card]:
        return [card for card in self.cards if card.playable(top)]

class Row
    def __init__(self, cards: list[Card]):
        {
            cards : [Card]
            ==
            put_card(Card)
            take_cards(Card) -> int
            ..
            save() -> json
            load(json)
        }
GameState o-- Row