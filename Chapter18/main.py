from play_card import Card, Deck, Hand


de = Deck()
de.shuffle_card()
num_hands = input("Enter number player: ")

list_hand = de.deal_hands(int(num_hands), 7)

for item in list_hand:
    # print(item["label"])
    # for i in item["cards"]:
    #     print("\t", i)
    # print()
    print(item)
    print("Have contains a flush: ", item.has_flush())

print(de)
