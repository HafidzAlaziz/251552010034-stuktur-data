from collections import deque

queue = deque()
# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print(f"Queue setelah enqueue: {repr(queue)}")

# Dequeue
d = queue.popleft()
print(f"Dequeue: {d}")
print(f"Queue setelah dequeue: {repr(queue)}")