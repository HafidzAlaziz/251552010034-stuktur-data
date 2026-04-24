class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def print_linked_list(node):
    while node:
        next_id = id(node.next) if node.next else None
        print(f"[{node.data} | {next_id}]-->", end="")
        node = node.next
    print("NULL")

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next = b
b.next = c
c.next = d
d.next = e

print_linked_list(a)