from game.deck import Deck
from player.dealer import Dealer
from player.player import Player

import utils.functions as func

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player 1")
        self.dealer = Dealer()

    def deal_initial_cards(self):
        """
        Deals the initial cards to each player/
        Each player is dealt 2 cards from the deck.
        Args: None
        Returns: None
        """

        for i in range(2):
            self.player.add_card_to_hand(
                self.deck.deal_card()
            )
            self.dealer.add_card_to_hand(
                self.deck.deal_card()
            )

    def print_hands(self, hide_dealer=False):
        """
        Prints the hands of the dealer and player along with hand values.
        Args: hide_dealer (bool, optional): If True, the dealer's cards and count will be hidden. Default is False.
        Returns: None
        """

        print(" +------------------------------------------------+")
        print("  DEALER")
        print(" +------------------------------------------------+")

        # draw dealer's cards
        func.hand_to_artwork(self.dealer.get_hand(), hide_dealer)

        # draw dealer's count
        print()
        if not hide_dealer:
            print(" Count: " + str(self.dealer.calculate_hand_value()))

        print()
        print(" +------------------------------------------------+")
        print(f"  {self.player.name.upper()}")
        print(f"  Balance: {self.player.balance - self.player.bet}$")
        print(f"  Current Bet: {self.player.bet}$")
        print(" +------------------------------------------------+")

        # draw player's cards
        func.hand_to_artwork(self.player.get_hand())

        # draw player's count
        print()
        print(" Count: " + str(self.player.calculate_hand_value()))

    def intro(self):
        """
        Displays the introductory screen for the game.
        Args: None
        Returns: None
        """
        func.clear_screen()
        func.print_logo()
        self.player.name = self.get_player_name()

    @staticmethod
    def get_player_name():
        """
        Static method to prompt the player to enter their name.
        Args: None
        Returns: str: The player's entered name.
        """
        while True:
            name = input("Welcome, Enter your name: ")
            if name.strip():  # Check if the name is not empty after stripping whitespace
                return name
            else:
                print("Please enter a valid name.")


    def draw_screen(self, hide_dealer=False):
        """
        Draws the game screen.
        Args: hide_dealer (bool, optional): If True, the dealer's hand will be hidden. Default is False.
        Returns: None
        """

        func.clear_screen()
        func.print_logo()
        self.print_hands(hide_dealer)

    def run(self):
        """
        Runs the main game loop.
        Args: None
        Returns: None
        """

        self.intro()
        while True:

            # New Game
            self.deck.get_new()
            self.player.clear_hand()
            self.dealer.clear_hand()

            # Place Bets
            self.bets()

            # Deal Cards
            self.deal_initial_cards()

            # redraw screen
            self.draw_screen(True)

            #round
            self.play()

            print()
            print(" ==================================================")
            play_again = input(" Do you want to play again? (y/n): ")
            if play_again.lower() != 'y':
                print()
                print("Thanks for playing!")
                break

    def bets(self):
        """
        Manages the betting phase of the game.
        Args: None
        Returns: None
        """

        func.clear_screen()
        func.print_logo()

        while True:
            print(f" {self.player.name}, your current balance is ${self.player.balance}")

            if self.player.last_bet > 0:
                bet_amount = input(f" Place your bet [${self.player.last_bet}]: ")
            else:
                bet_amount = input(f" Place your bet: ")

            if bet_amount.isdigit():
                if self.player.place_bet(int(bet_amount)):
                    break
            elif bet_amount.strip() == "" and self.player.last_bet > 0:
                if self.player.place_bet(self.player.last_bet):
                    break
            else:
                print("Invalid bet. Please enter a valid number amount.")

    def play(self):
        """
        Manages the gameplay phase of the game.
        Args: None
        Returns: None
        """

        while True:
            player_hand_value = self.player.calculate_hand_value()
            dealer_hand_value = self.dealer.calculate_hand_value()

            if len(self.player.get_hand()) == 2 and player_hand_value == 21:
                self.player.win_bet()

                # redraw screen
                self.draw_screen()

                func.print_alert("Blackjack! You win!")
                break

            print()
            print(" ==================================================")
            player_choice = input(" Do you want to hit or stand? (h/s): ")

            if player_choice.lower() == 'h':  # Player chooses to hit
                self.player.add_card_to_hand(self.deck.deal_card())

                # redraw screen
                self.draw_screen(True)

                player_hand_value = self.player.calculate_hand_value()
                if player_hand_value > 21:
                    self.player.lose_bet()
                    # redraw screen
                    self.draw_screen()
                    func.print_alert("Bust! You lost.")
                    break
            elif player_choice.lower() == 's':  # Player chooses to stand
                # Dealer's turn simple AI

                # redraw screen
                self.draw_screen()

                while self.dealer.take_turn(player_hand_value) == Dealer.HIT:
                    self.dealer.add_card_to_hand(self.deck.deal_card())

                    # redraw screen
                    self.draw_screen()

                    dealer_hand_value = self.dealer.calculate_hand_value()

                if dealer_hand_value > 21 or dealer_hand_value < player_hand_value:
                    self.player.win_bet()
                    func.print_alert("You win!")
                elif dealer_hand_value == player_hand_value:
                    self.player.push()
                    func.print_alert("It's a tie!")
                else:
                    self.player.lose_bet()
                    func.print_alert("You lose!")
                break
