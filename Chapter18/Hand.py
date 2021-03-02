from Deck import Deck


class Hand(Deck):
    def __init__(self, label=""):
        self.cards = []
        self.label = label

    def __str__(self):
        return self.label + ":\n" + "\n".join(str(item) for item in self.cards)
