from Card import Card


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


de = Deck()

print(de)
