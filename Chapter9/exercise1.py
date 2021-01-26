# print(os.path.curdir)
# print(os.path.isdir("."))

# fin = open('D:\Python\Example\Exercise\Chapter9\words.txt')
fin = open('.\Chapter9\words.txt')


for line in fin:
    word = line.strip()
    if len(word ) >= 20:
        print(word,len(word))
