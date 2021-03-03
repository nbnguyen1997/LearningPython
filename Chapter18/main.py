from play_card import Card, Deck, Hand


# num_hands = input("Enter number player: ")
num_hands = 7


hist_classify = {}

for i in range(10000):
    de = Deck()
    de.shuffle_card()
    list_hand = de.deal_hands(int(num_hands), 7)
    for item in list_hand:
        # print(item["label"])
        # for i in item["cards"]:
        #     print("\t", i)
        # print()
        hist_classify[item.classify()] = hist_classify.get(
            item.classify(), 0) + 1
        # print(item)
        # print("Have contains a flush: ", item.has_flush())
print("The number of times various classifications appear in 70000 hand:")
for key in hist_classify:
    print(key, hist_classify[key])
# print(de)
