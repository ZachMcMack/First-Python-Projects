import random


class Deck:

    def __init__(self):
        self.deck = []

        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.num_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        
        for num, value in enumerate(self.values):
            for suit in self.suits:
                self.deck.append((value, suit, self.num_values[num]))

    def draw_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def draw_cards(self, num_cards):
        if num_cards > len(self.deck):
            print("Not enough cards in deck.")
        elif 2 > num_cards or num_cards > 5:
            print("Must draw between 2 and 5 cards.")
        return [self.draw_card() for i in range(num_cards)]
        
    def get_order(self):
        return self.order

    def print_deck(self):
        print('deck:')
        for card in self.deck:
            print(card)