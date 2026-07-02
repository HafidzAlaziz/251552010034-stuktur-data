# Hapus semua elemen duplikat dari list
# Tanpa  menggunakan set(), tetap 
# mempertahankan urutan asli:
# data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

data_bersih = []
for i in data:
    if i not in data_bersih:
        data_bersih.append(i)

print("Data asli:", data)
print("Data bersih:", data_bersih)
