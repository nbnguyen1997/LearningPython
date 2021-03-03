from Deck import Deck
import random
from Card import Card


class Card:
    def __init__(self, rank_id, suit_id):
        self.rank = rank_id
        self.suit = suit_id

    def __str__(self):
        return "%s of %s" % (rank_names[self.rank], suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit

        return t1 < t2


suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_names = [None, "Ace", "2", "3", "4", "5", "6",
              "7", "8", "9", "10", "Jack", "Queen", "King"]


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
            # hand = dict()  # because we cannot call the Hand class
            # hand["label"] = "Hand " + str(hand_id)
            # hand["cards"] = []
            hand = Hand("Hand %s" % hand_id)
            hands.append(hand)

        for i in range(num_cards_per_hand):
            for hand in hands:
                self.move_card(hand, 1)

        return hands


class Hand(Deck):
    def __init__(self, label=""):
        self.cards = []
        self.label = label

    def __str__(self):
        return self.label + ":\n\t" + "\n\t".join(str(item) for item in self.cards)
