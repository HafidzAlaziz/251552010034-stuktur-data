class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

current = a
while current :
    print(f"Node @ {id(current)} | Data:{current.data} | Next:{id(current.next) if current.next else None}")
    current = current.next