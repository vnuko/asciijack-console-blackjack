class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bet = 0
        self.last_bet = 0
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand

    def calculate_hand_value(self):
        count = 0
        num_aces = 0

        for card in self.hand:
            if card.rank.isdigit(): # 1-10
                count += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']: # J, Q, K
                count += 10
            else: # A
                num_aces += 1

        for _ in range(num_aces):
            if count + 11 <= 21:
                count += 11
            else:
                count += 1

        return count

    def clear_hand(self):
        self.hand.clear()

    def place_bet(self, amount):
        if 0 < amount <= self.balance:
            self.bet = self.last_bet = amount
            return True
        else:
            print("Not enough funds. Try again!")
            return False

    def win_bet(self):
        self.balance += self.bet
        self.bet = 0

    def lose_bet(self):
        self.balance -= self.bet
        self.bet = 0

    def push(self):
        print("It's a push! Your bet is returned.")
        self.bet = 0
