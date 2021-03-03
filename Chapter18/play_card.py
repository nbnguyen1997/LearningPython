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
        t2 = other.get_rank(), other.get_suit()

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
        self.__rank_hist = {}
        self.__suit_hist = {}
        self.__classify = {}

    def set_card(self, card):
        if isinstance(card, Card):
            self.__cards.append(card)
        else:
            raise TypeError("TypeError exception thrown")

    def get_cards(self):
        return self.__cards

    def __str__(self):
        self.__cards.sort()
        # self.poker_hand()
        return self.__label + ":\n\t" + "\n\t".join(str(item) for item in self.__cards) + "\n\t\t" + self.classify()

    def poker_hand(self):
        # return "\n\t\tPair: %r\n\t\tTwo pair: %r\n\t\tThree: %r\n\t\tFlush: %r\n\t\tFull house: %r\n\t\tFour: %r\n" % (self.has_pair(), self.has_twopair(), self.has_three(), self.has_flush(), self.has_fullhouse(), self.has_four())
        self.classify_hist()
        return "\n\t\t"+"\n\t\t".join(str(item) for item in list(self.__classify.items()))

    def suit_hist(self):
        # self.__suit_hist = dict()

        for card in self.__cards:
            self.__suit_hist[card.get_suit()] = self.__suit_hist.get(
                card.get_suit(), 0) + 1

    def rank_hist(self):
        # self.__rank_hist = dict()

        for card in self.__cards:
            self.__rank_hist[card.get_rank()] = self.__rank_hist.get(
                card.get_rank(), 0) + 1

    def find_criteria_card(self, *number_card):
        result = []

        if len(self.__rank_hist) == 0:
            self.rank_hist()
        list_left_over = list(self.__rank_hist.values())
        list_left_over.sort()
        list_num = list(number_card)
        list_num.sort()
        for num in list_num:
            res = self.find_num(list_left_over, num)
            if res == None:
                return False
            else:
                list_left_over.remove(res)
        return True

    def find_num(self, list_num, num):
        for val in list_num:
            # Truong hop tim thay 3(hoac 4) cay cung loai thi has_pair() van dung
            if val >= num:
                return val
        return None

    def has_flush(self):
        self.suit_hist()
        for val in self.__suit_hist.values():
            if val >= 5:
                return True

        return False

    def has_pair(self):
        return self.find_criteria_card(2)

    def has_twopair(self):
        return self.find_criteria_card(2, 2)

    def has_three(self):
        return self.find_criteria_card(3)

    def has_four(self):
        return self.find_criteria_card(4)

    def has_fullhouse(self):
        return self.find_criteria_card(3, 2)

    def classify_hist(self):
        hist = {
            "Pair": self.has_pair(),
            "Two pair": self.has_twopair(),
            "Three": self.has_three(),
            "Flush": self.has_flush(),
            "Full house": self.has_fullhouse(),
            "Four": self.has_four()
        }
        self.__classify = hist

    def classify(self):
        if len(self.__classify) == 0:
            self.classify_hist()
        result = "High card"
        for key in list_classify:
            if self.__classify[key] == True:
                result = key
        return result


list_classify = ["Pair", "Two pair", "Three", "Flush", "Full house", "Four"]
