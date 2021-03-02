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
