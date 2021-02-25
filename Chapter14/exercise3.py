import os


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


def request_1(path, suffix):

    result = walk(path)

    for link in result:
        if link.endswith(suffix):
            print(link)


ps = os.getcwd()
# print(os.listdir(ps))
request_1(ps, ".txt")
