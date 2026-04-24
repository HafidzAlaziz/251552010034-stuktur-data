class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data): # ini nambah di depan
    new_node = Node(data)
    new_node.next = head
    return new_node

def insert_at_end(head, data): # ini nambah di belakang
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_after_node(prev_node, data):
    if not prev_node:
        print("Node sebelumnya tidak ditemukan.")
        return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

    
head = Node("Ikan")
head = insert_at_beginning(head, "Cupang") # tambah di depan
head = insert_at_end(head, "Lele") # tambah di belakang
insert_after_node(head, "Gurame") # tambah setelah head
def print_linked_list(head):
    while head:
        print(f"[{head.data}] -->", end="")
        head = head.next
    print("NULL")

print_linked_list(head)