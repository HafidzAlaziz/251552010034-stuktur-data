def balik_string(teks): # Fungsi membalik string
    stack = [] 

# Langkah 1: PUSH setiap karakter ke stack
    for char in teks:
        stack.append(char) # Push satu per satu

# Langkah 2: POP karakter — keluar urutan terbalik (LIFO!)
    hasil = ''
    while stack: # selama stack tidak
        hasil += stack.pop() # pop = ambil dari TOP
    return hasil

# === Contoh Penggunaan ===
print(balik_string('kapal terbang')) 
print(balik_string('hello world')) 
print(balik_string('Python'))