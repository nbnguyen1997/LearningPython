import os, hashlib


def walk(directory):
    names = list()

    for name in os.listdir(directory):
        if name == ".git":
            continue
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))

    return names


def request_1(list_path, suffix):

    for link in list_path:
        if link.endswith(suffix):
            print(link)


def checksum_file(list_path, suffix):
    resutl = list()

    for index_1 in range(len(list_path) - 1):
        if list_path[index_1].endswith(suffix):
            for index_2 in range(index_1 + 1, len(list_path)):
                if list_path[index_2].endswith(suffix):
                    file_1 = open(list_path[index_1], "rb")
                    file_2 = open(list_path[index_2], "rb")
                    hash_1 = hashlib.md5(file_1.read()).hexdigest()
                    hash_2 = hashlib.md5(file_2.read()).hexdigest()
                    if hash_1 == hash_2:
                        resutl.append((hash_1, hash_2))

    if len(resutl) == 0:
        print("No file (%s) with the same content" % suffix)
    else:
        for item1, item2 in resutl:
            print(item1, end=" ")
            print(item2)


ps = os.getcwd()
list_path = walk(ps)
# print(os.listdir(ps))
request_1(list_path, ".txt")

checksum_file(list_path, ".txt")
