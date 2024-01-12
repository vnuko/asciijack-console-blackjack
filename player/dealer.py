from player.person import Person

class Dealer(Person):
    HIT = 'hit'
    STAND = 'stand'

    def __init__(self):
        super().__init__("Dealer", 0)

    def take_turn(self, player_hand_value):
        dealer_hand_value = self.calculate_hand_value()

        if dealer_hand_value < 17:
            return self.HIT
        elif 17 <= dealer_hand_value < player_hand_value:
            return self.HIT
        else:
            return self.STAND
