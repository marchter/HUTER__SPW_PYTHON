class Arraylist:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def append(self, e):
        self.list.append(e)

    def addFront(self,e):
        self.list.insert(0,e)

    def get(self, index):
        return self.list.index(index)

    def getFirst(self):
        return self.list[0]

    def getLength(self):
        return len(self.list)

    def print(self):
        print(self.list)

    def clear(self):
        self.list.clear()

    def deleteFirst(self):
        self.list.pop(0)

    def search(self,e):
        for i in self.list:
            if i is e:
                return i

    def sort(self):
        self.list.sort()

def main():
    a = Arraylist()

    a.print()
    print(a.isEmpty())
    print(a.getLength())

    print("-" * 50)

    a.append(10)
    a.append(2)
    a.append(7)

    a.print()
    print(a.isEmpty())
    print(a.getLength())

    print("-" * 50)

    a.addFront(69)
    a.print()
    print(a.get(2))

    print("-" * 50)
    a.deleteFirst()
    a.sort()
    a.print()



if __name__ == "__main__":
    main()
