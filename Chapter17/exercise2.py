class Kangaroo:
    def __init__(self, name, pouch_contents=[]):
        self.name = name
        self.pouch_contents = pouch_contents

    def __init__(self, name, pouch_contents=None):
        self.name = name
        if pouch_contents == None:
            pouch_contents = []
        self.pouch_contents = pouch_contents

    def put_in_pouch(self, ob):
        self.pouch_contents.append(ob)

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return "\n".join(t)


kanga = Kangaroo("kan")
roo = Kangaroo("roo")
af = Kangaroo("af")
kanga.put_in_pouch("Nguyen")
kanga.put_in_pouch(roo)
kanga.put_in_pouch(af)
# ar = ["asd", kanga.pouch_contents]
print(kanga)
# for item in kanga.pouch_contents:
#     print(item)
