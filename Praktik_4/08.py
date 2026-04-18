from collections import deque

queue = deque() # antrian kosong

# Pelanggan datang (Enqueue dari belakang)
queue.append('Andi') 
queue.append('Budi') 
queue.append('Citra') 
queue.append('Dina') 
queue.append('Eka')
queue.append('Fajar')

print('Antrian awal:', list(queue))
print('Yang pertama dilayani:', queue[0]) 
print('--- Mulai melayani ---')

nomor = 1
while queue: # selama ada antrian
    pelanggan = queue.popleft() 
    print(f'[{nomor}] Melayani: {pelanggan}')
    if queue:
        print(f' Antrian: {list(queue)}')
    nomor += 1
    
print('Semua pelanggan telah dilayani!')