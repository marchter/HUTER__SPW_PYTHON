class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


def do2Times(func):
    def wrapper2Times(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper2Times


def doXTimes(func):
    def wrapperXTimes(*args, **kwargs):
        for i in range(args[1]):
            func(*args, **kwargs)

    return wrapperXTimes


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head is None

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def append(self, data):
        e = Element(data)
        if self.isEmpty():
            self.head = e
            self.tail = e
        else:
            self.tail.next = e
            self.tail = e
        self.length += 1

    def addFront(self, data):
        e = Element(data)
        if self.isEmpty():
            self.append(data)
            return
        e.next = self.head
        self.head = e

        self.length += 1

    def add(self, data, index):
        e = Element(data)
        current = self.head

        for i in range(index):
            current = current.next

        e.next = current.next
        current.next = e

        self.length += 1

    @do2Times
    def append2Times(self, data):
        self.append(data)

    # schwierigkeiten gehabt wegen nicht wissen wie man times in wrapper usen kann
    @doXTimes
    def appendXTimes(self, times, data):
        self.append(data)

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def delFirst(self):
        self.head = self.head.next
        self.length -= 1

    def delElement(self, el):

        current = self.head
        while current is not None:
            if current.next == Element(el):
                current.next = current.next.next
                self.length -= 1
                break
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None

        self.length = 0

    # meh
    def search(self, el):
        current = self.head
        while current is not None:
            if current == Element(el):
                return current
            current = current.next
        return None

    def sort_int(self):
        current = self.head
        while current.next:
            if current.data > current.next.data:
                current.data, current.next.data = current.next.data, current.data
                current = self.head
            else:
                current = current.next

    def sort_string_length(self):
        current = self.head
        while current.next:
            if len(current.data) > len(current.next.data):
                current.data, current.next.data = current.next.data, current.data
                current = self.head
            else:
                current = current.next


def main():
    l1 = List()

    l1.append(1)
    l1.append(2)
    l1.append(3)

    l1.addFront(2)

    l1.append2Times(4)
    l1.appendXTimes(3, 0)

    l1.add(99, 1)
    l1.print()

    print("-" * 50)

    l1.delFirst()

    l1.delElement(0)

    l1.print()
    print("-" * 50)

    print(l1.length)
    print(l1.get(1).data)

    print("-" * 50)
    l1.sort_int()
    l1.print()

    print("-" * 50)

    l2 = List()
    l2.append("huter")
    l2.append("hirsch")
    l2.append("asdf")
    l2.sort_string_length()
    l2.print()

    print("-" * 50)

    l1.clear()


if __name__ == '__main__':
    main()
