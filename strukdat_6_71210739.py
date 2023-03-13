class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Dae:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addElementHead(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def addElementTail(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def maju(self, steps):
        if steps >= self.size:
            print(self.tail.data)
            return
        node = self.head
        for i in range(steps):
            node = node.next
        print(node.data)

    def mundur(self, steps):
        if steps >= self.size:
            print(self.head.data)
            return
        node = self.tail
        for i in range(steps):
            node = node.prev
        print(node.data)


linkedlist = Dae()
linkedlist.addElementHead("Jogja")  # Jogja
linkedlist.addElementHead("Jakarta")  # Jakarta - Jogja
linkedlist.addElementTail("Bali")  # Jakarta - Jogja - Bali
linkedlist.addElementTail("Bandung")  # Jakarta - Jogja - Bali - Bandung

linkedlist.maju(2)  # output: Bali
linkedlist.mundur(1)  # output: Jogja
linkedlist.maju(5)  # output: Bali
linkedlist.mundur(3)  # output: Bandung
