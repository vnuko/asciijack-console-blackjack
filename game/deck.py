import random

from game.card import Card


class Deck:
    SUITS = ["CLUBS", "DIAMONDS", "HEARTS", "SPADES"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    cards = []

    def __init__(self):
        self.get_new()

    def get_new(self):
        self.cards.clear()

        for suit in self.SUITS:
            for rank in self.RANKS:
                self.cards.append(Card(suit, rank))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
