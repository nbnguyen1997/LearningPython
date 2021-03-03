from play_card import Card, Deck, Hand


# num_hands = input("Enter number player: ")
num_hands = 7


def make_string(key, number, total):
    lenth_key = len(key)
    lenth_num = len(str(number))
    num_probability = 100*number/total
    lenth_space = 15 - lenth_key - lenth_num
    lenth_space1 = 6 - len(str(num_probability))
    space = " "*lenth_space
    space1 = " "*lenth_space1
    print("%s:%s%d\tprobabilities: %s %2.2f" %
          (key, space, number, space1, num_probability))


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
    # print("\t%s :%d \t (probabilities:%.2f)" %
    #       (key, hist_classify[key], 100*(hist_classify[key]/70000)))
    make_string(key, hist_classify[key], 70000)
# print(de)
