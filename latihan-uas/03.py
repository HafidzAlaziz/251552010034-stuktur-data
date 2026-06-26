class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def tampilkan(self):
        if not self.head:
            return
        temp = self.head
        hasil = []
        while True:
            hasil.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(f"Circular Linked List: {' -> '.join(hasil)} -> (kembali ke head)")

cll = CircularLinkedList()
cll.tambah(10)
cll.tambah(20)
cll.tambah(30)
cll.tampilkan()