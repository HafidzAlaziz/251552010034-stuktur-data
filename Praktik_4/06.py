from collections import deque # Import deque dari modul collections

# Buat antrian/list kosong 
queue = deque() # 

# ENQUEUE  tambah ke belakang (REAR) 
queue.append('budi') 
queue.append('Andi') 
queue.append('opet') 

print('Queue:', queue) 

# lihat elemen DEPAN tanpa hapus 
front = queue[0] 
print('Peek:', front) 

#  hapus dari DEPAN 
keluar = queue.popleft() 
print('Dequeue:', keluar) 
print('Queue:', queue)

# ukuran atau isi
print('Kosong?', len(queue)==0) # Kosong = False
print('Ukuran:', len(queue)) # Ukuran