from Deck import Deck
from Hand import Hand

de = Deck()

list_hand = de.deal_hands(4, 13)

for item in list_hand:
    print(item["label"])
    for i in item["cards"]:
        print("\t", i)
    print()
