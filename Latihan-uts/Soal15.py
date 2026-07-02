# 15. Balikkan urutan node pada linked list
# (reverse linked list) secara in-place
# tanpa membuat list baru.

# Output yang diharapkan:
# Sebelum: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Sesudah: 5 -> 4 -> 3 -> 2 -> 1 -> None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        hasil = ""
        while current:
            hasil += str(current.data) + " -> "
            current = current.next
        hasil += "None"
        print(hasil)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

ll = LinkedList()
for angka in [1, 2, 3, 4, 5]:
    ll.append(angka)

print("Sebelum:", end=" ")
ll.display()

# Memanggil fungsi reverse
ll.reverse()

print("Sesudah:", end=" ")
ll.display()
