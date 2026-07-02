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
    
    def hapusbelakang(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
    def tampilkan(self, label):
        temp = self.head
        res = []
        while temp :
            res.append(str(temp.data))
            temp = temp.next
        res.append("None")
        print(f"{label}: {' -> ' .join(res)}")

ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.tambah(val)
ll.tampilkan("Sebelum")
ll.hapusbelakang()
ll.tampilkan("Sesudah")
