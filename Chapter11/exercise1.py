fin = open(".\Chapter9\words.txt")


def create_dict():
    d = dict()
    for item in fin:
        word = item.strip()
        d[word] = ""
    return d


def main():
    d = create_dict()
    word = "schooled"
    if word in d:
        print(word)
    else:
        print("not found")


if __name__ == "__main__":
    main()
