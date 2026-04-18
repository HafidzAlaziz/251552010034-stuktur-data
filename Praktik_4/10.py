import heapq 

pq = [] 

heapq.heappush(pq, (3, 'Task C - Rendah')) 
heapq.heappush(pq, (1, 'Task A - URGENT')) 
heapq.heappush(pq, (2, 'Task B - Medium')) 

print('Priority Queue:', pq)


while pq:
    prioritas, task = heapq.heappop(pq) 
    print(f'[Prioritas {prioritas}] Proses: {task}')