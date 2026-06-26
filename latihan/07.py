class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def tambah_depan(self, data):
        new_node = DNode(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def tambah_belakang(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def tampilkan_maju(self):
        temp = self.head
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        res.append("None")
        print(f"Maju: {' <-> '.join(res)}")

    def tampilkan_mundur(self):
        temp = self.head
        if not temp: return
        while temp.next:
            temp = temp.next
        res = []
        while temp:
            res.append(str(temp.data))
            temp = temp.prev
        res.append("None")
        print(f"Mundur: {' <-> '.join(res)}")

dll = DoublyLinkedList()
dll.tambah_depan(3)
dll.tambah_belakang(1)
dll.tambah_belakang(2)
dll.tambah_belakang(3)
dll.tampilkan_maju()
dll.tampilkan_mundur()