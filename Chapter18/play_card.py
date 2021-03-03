from Deck import Deck
import random
from Card import Card


class Card:
    def __init__(self, rank_id, suit_id):
        self.__rank = rank_id
        self.__suit = suit_id

    def set_rank(self, rank):
        if rank not in range(1, 14):
            raise ValueError("ValueError exception thrown")
        else:
            self.__rank = rank

    def get_rank(self):
        return self.__rank

    def set_suit(self, suit):
        if suit not in range(0, 4):
            raise ValueError("ValueError exception thrown")
        else:
            self.__suit = suit

    def get_suit(self):
        return self.__suit

    def __str__(self):
        return "%s of %s" % (rank_names[self.__rank], suit_names[self.__suit])

    def __lt__(self, other):
        t1 = self.__rank, self.__suit
        t2 = other.get_rank, other.get_suit

        return t1 < t2


suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_names = [None, "Ace", "2", "3", "4", "5", "6",
              "7", "8", "9", "10", "Jack", "Queen", "King"]


class Deck:
    def __init__(self):
        self.__cards = []
        for suit in range(0, 4):
            for rank in range(1, 14):
                card = Card(rank, suit)
                self.set_card(card)

    def set_card(self, card):
        if isinstance(card, Card):
            self.__cards.append(card)
        else:
            raise TypeError("TypeError exception thrown")

    def get_cards(self):
        return self.__cards

    def __str__(self):
        return "\n".join(str(item) for item in
                         self.__cards)

    def pop_card(self):
        return self.__cards.pop()

    def add_card(self, card):
        self.set_card(card)

    def shuffle_card(self):
        random.shuffle(self.__cards)

    def sort(self):
        self.__cards.sort()

    def move_cards(self, hand, num):
        if isinstance(hand, Deck):
            for i in range(num):
                hand.add_card(self.pop_card())
        else:
            hand["cards"].append(self.pop_card())

    def deal_hands(self, num_hands, num_cards_per_hand):
        if num_hands * num_cards_per_hand > 52:
            raise ValueError("ValueError exception thrown")
        hands = []
        for hand_id in range(num_hands):
            # hand = dict()  # because we cannot call the Hand class
            # hand["label"] = "Hand " + str(hand_id)
            # hand["cards"] = []
            hand = Hand("Hand %s" % hand_id)
            hands.append(hand)

        for i in range(num_cards_per_hand):
            for hand in hands:
                self.move_cards(hand, 1)

        return hands


class Hand(Deck):
    def __init__(self, label=""):
        self.__cards = []
        self.__label = label

    def set_card(self, card):
        if isinstance(card, Card):
            self.__cards.append(card)
        else:
            raise TypeError("TypeError exception thrown")

    def get_cards(self):
        return self.__cards

    def __str__(self):
        return self.__label + ":\n\t" + "\n\t".join(str(item) for item in self.__cards)

    def suit_hist(self):
        self.__suit_hist = dict()

        for card in self.__cards:
            self.__suit_hist[card.get_suit] = self.__suit_hist.get(
                card.get_suit, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.__suit_hist.values():
            if val >= 5:
                return True

        return False
