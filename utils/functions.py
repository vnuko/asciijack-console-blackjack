import os
import artwork.cards as blackjack_cards
import artwork.logo as blackjack_logo

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_logo():
    print(blackjack_logo.LOGO)

def print_alert(message):
    print()
    print("+-===============-+")
    print(f" {message} ")
    print("+-===============-+")

def card_to_artwork(suit, rank):
    if suit.lower() == 'clubs':
        return blackjack_cards.CLUBS[rank]
    elif suit.lower() == 'diamonds':
        return blackjack_cards.DIAMONDS[rank]
    elif suit.lower() == 'hearts':
        return blackjack_cards.HEARTS[rank]
    elif suit.lower() == 'spades':
        return blackjack_cards.SPADES[rank]

def card_back_artwork():
    return blackjack_cards.BACK

# Function to display cards side by side
def hand_to_artwork(hand, hide_dealer=False):
    lines = []
    for idx, card in enumerate(hand):
        if hide_dealer == True and idx == 1:
            card_artwork = card_back_artwork()
        else:
            card_artwork = card_to_artwork(card.suit, card.rank)

        lines.append(card_artwork.split('\n'))

    # Iterate through lines on all cards and display them side by side
    for l in zip(*lines):
        print("  ".join(l))
