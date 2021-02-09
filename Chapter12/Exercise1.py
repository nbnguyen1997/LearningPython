def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.
    s: string
    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    result = []
    for freq, x in t:
        result.append(x)

    return result
    

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""

    return open(filename,"r",encoding="utf8").read()


if __name__ == '__main__':
    string = read_file('.\Chapter12\emma.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)