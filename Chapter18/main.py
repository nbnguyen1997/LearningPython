from play_card import Card, Deck, Hand

de = Deck()
de.shuffle_card()
list_hand = de.deal_hands(4, 13)

for item in list_hand:
    # print(item["label"])
    # for i in item["cards"]:
    #     print("\t", i)
    # print()
    print(item)
