import deck
import hand_checker
from tabulate import tabulate

def print_hand(hand):
    print(f"Your hand is:")
    for card in hand:
        print(f"{card[0]} of {card[1]}s")

def deal_hands(num_players, deck):
    return [deck.draw_cards(5) for _ in range(num_players)]

def test_many_hands(check_func, hand_name):
    hand_array = []
    counter = 0
    for _ in range(1000):
        counter += 1
        test_deck = deck.Deck()
        test_hand = test_deck.draw_cards(5)
        #print(test_hand)
        #print(hand_checker.multiples(test_hand))
        hand_array.append([f"{card[0]} of {card[1]}s" for card in test_hand] + hand_checker.determine_code(test_hand))
    hand_array = sorted(hand_array, key=lambda x:x[6], reverse=True)
    return hand_array

my_deck = deck.Deck()

#hand = my_deck.draw_cards(5)
#my_deck.print_deck()

print(tabulate(test_many_hands(hand_checker.straight, "straight")))