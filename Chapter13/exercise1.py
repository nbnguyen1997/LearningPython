import string

"""filetest.txt
Emma Woodhouse, handsome, clever, and rich, with a comfortable home
and happy disposition, seemed to unite some of the best blessings of
existence; and had lived nearly twenty-one years in the world with very
little to distress or vex her.

She was the youngest of the two daughters of a most affectionate,
indulgent father; and had, in consequence of her sister's marriage, been
mistress of his house from a very early period. Her mother had died
too long ago for her to have more than an indistinct remembrance of
her caresses; and her place had been supplied by an excellent woman as
governess, who had fallen little short of a mother in affection."""

fin = open(r".\Chapter13\filetest.txt", encoding="utf-8")
st = fin.read()


def split_string():
    resutl = []

    resutl = st.split()

    for item in resutl:
        if item[-1] in string.punctuation:
            print(item[:-1].lower())
        else:
            print(item.lower())
        # print(len(item), item, item[:-1])


split_string()
# print(string.whitespace)
