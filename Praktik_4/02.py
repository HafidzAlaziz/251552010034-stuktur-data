class Kardus:                                            # membuat nama bungkusan yg bernama Stack
    def __init__(self):                                  # Konstruktor (inisialisasi)
        self.items = []                                  # List kosong sebagai penyimpan
        
    def push(self, item):                                # Tambah elemen ke atas
        self.items.append(item)
        
    def pop(self):                                       # Hapus & kembalikan elemen atas
        if not self.is_empty():
            return self.items.pop()
        return 'Stack kosong!'                           # Guard: cegah error
    
    def peek(self):                                      # Lihat elemen atas
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):                                  # True jika kosong
        return len(self.items) == 0
    
    def size(self):                                      # Jumlah elemen
        return len(self.items)
    
    def __str__(self):                                   # Cetak isi stack
        return str(self.items)
    
# Contoh penggunaan
a = Kardus() # panggil objek 

a.push('makanan')
a.push('minuman')
a.push('snack')

print(a)

print("paling atas:",a.peek()) # melihat elemen teratas tanpa menghapusnya

print("yang dihapus:",a.pop())

print(a) 

print("paling atas :",a.peek())

print(a.size()) 
print(a.is_empty())