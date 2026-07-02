# 14. Pada linked list: 10->20->30->40->50
# Buat method delete(nilai) yang menghapus
# node dengan nilai tertentu.

# Hapus node bernilai 30, lalu tampilkan
# linked list sebelum dan sesudah.

# Output yang diharapkan:
# Sebelum: 10 -> 20 -> 30 -> 40 -> 50 -> None
# Sesudah: 10 -> 20 -> 40 -> 50 -> None

# Struktur Dasar Linked List (Sudah disiapkan)
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

    def delete(self, nilai):
        if self.head is None:
            return
        if self.head.data == nilai:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != nilai:
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        
ll = LinkedList()
for angka in [10, 20, 30, 40, 50]:
    ll.append(angka)

print("Sebelum:", end=" ")
ll.display()

ll.delete(30)

print("Sesudah:", end=" ")
ll.display()
