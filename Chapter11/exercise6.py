link_dictionary = ".\Chapter11\c06d.txt"
def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.
    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".
    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def make_word_dict():
    """Read. the words in words.txt and return a dictionary
    that contains the words as keys."""
    d = dict()
    fin = open('.\Chapter9\words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def homophones(a, b, phonetic):
    """Checks if words two can be pronounced the same way.
    If either word is not in the pronouncing dictionary, return False
    a, b: strings
    phonetic: map from words to pronunciation codes
    """
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    """Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation.
    word: string
    word_dict: dictionary with words as keys
    phonetic: map from words to pronunciation codes
    """
    word1 = word[1:] 
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True


if __name__ == '__main__':
    phonetic = read_dictionary(link_dictionary)
    word_dict = make_word_dict()

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])