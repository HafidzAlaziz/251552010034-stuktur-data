class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def hapus(self, nilai):
        temp = self.head
        if temp and temp.data == nilai:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != nilai:
            prev = temp
            temp = temp.next
        if not temp: return
        prev.next = temp.next

    def tampilkan(self, label):
        temp = self.head
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        res.append("None")
        print(f"{label}: {' -> '.join(res)}")

ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.tambah(val)

ll.tampilkan("Sebelum")
ll.hapus(30)
ll.tampilkan("Sesudah")