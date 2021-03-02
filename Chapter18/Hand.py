from Deck import Deck


class Hand(Deck):
    def __init__(self, label=""):
        self.cards = []
        self.label = label

    def __str__(self):
        return self.label + ":\n" + "\n".join(str(item) for item in self.cards)


de = Deck()

hs = Hand("nguyen")

de.move_card(hs, 4)

print(de)
print("\n")
print(hs)

hs.move_card(de, 2)

print(de)
print("\n")
print(hs)
