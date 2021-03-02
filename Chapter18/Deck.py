from Card import Card

import random


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(0, 4):
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.cards.append(card)

    def __str__(self):
        return "\n".join(str(item) for item in
                         self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle_card(self):
        random.shuffle(self.cards)

    def sort_card(self):
        self.cards.sort()

    def move_card(self, hand, num):
        if isinstance(hand, Deck):
            for i in range(num):
                hand.add_card(self.pop_card())
        else:
            hand["cards"].append(self.pop_card())

    def deal_hands(self, num_hands, num_cards_per_hand):
        hands = []
        for hand_id in range(num_hands):
            hand = dict()  # because we cannot call the Hand class
            hand["label"] = "Hand " + str(hand_id)
            hand["cards"] = []
            hands.append(hand)

        for i in range(num_cards_per_hand):
            for hand in hands:
                self.move_card(hand, 1)

        return hands
