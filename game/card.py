class Card:
    def __init__(self, suit, rank):
        self.suit = suit # type: str
        self.rank = rank # type: str

    def __str__(self):
        return f"{self.rank} of {self.suit}"
