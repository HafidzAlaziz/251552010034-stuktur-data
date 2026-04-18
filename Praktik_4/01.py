stack = [] # bungkusan kosong

print('Awal:', stack) # disini menampilkan bungkusan yg masih kosong

# PUSH — tambah elemen ke atas stack
stack.append('A') 
stack.append('B') 
stack.append('C') 

print('Setelah push:', stack) # menampilkan isi stack setelah ditambahkan elemen A, B, dan C

# PEEK — lihat elemen teratas tanpa hapus
top = stack[-1]
print('Peek:', top)

# POP — hapus dan ambil elemen teratas
popped = stack.pop() 
print('Dipop:', popped) 
print('Stack:', stack) 

# PEEK — lihat elemen teratas tanpa hapus
top = stack[-1]
print('Peek:', top)

popped = stack.pop() 
print('Dipop:', popped) 
print('Stack:', stack) 

# PEEK — lihat elemen teratas tanpa hapus
top = stack[-1]
print('Peek:', top)

popped = stack.pop() 
print('Dipop:', popped) 
print('Stack:', stack) 

# IS EMPTY & SIZE
print('Kosong?', len(stack)==0) # Kalo kosong false, kalo tidak kosong true
print('Ukuran:', len(stack)) # Ukuran akhir